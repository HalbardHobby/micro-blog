package main

import (
	"bytes"
	"encoding/json"
	"log"
	"net/http"
	"strings"

	"github.com/labstack/echo/v4"
)

type EventMessage struct {
	Type string          `json:"type"`
	Data json.RawMessage `json:"data"`
}

type CommentData struct {
	Id      string `json:"id"`
	Content string `json:"content"`
	PostId  string `json:"postId"`
	Status  string `json:"status"`
}

func receiveEvent(c echo.Context) error {
	e := new(EventMessage)
	if err := c.Bind(&e); err != nil {
		log.Print(err)
		return err
	}

	log.Print(e.Type)

	if e.Type == "CommentCreated" {
		var data CommentData
		json.Unmarshal([]byte(e.Data), &data)
		log.Print(data.Content)

		data.Status = "appproved"
		if strings.Contains(data.Content, "obscene") {
			data.Status = "rejected"
		}

		json_res, _ := json.Marshal(data)
		event := EventMessage{"CommentModerated", json_res}
		res, _ := json.Marshal(event)
		log.Print(string(res))

		_, err := http.Post("http://event-bus-service:4999/events/",
			"application/json",
			bytes.NewBuffer(res))

		if err != nil {
			log.Print(err)
		}
	}
	return c.NoContent((http.StatusOK))
}

func main() {
	e := echo.New()

	e.POST("/events/", receiveEvent)

	e.Logger.Fatal(e.Start(":5003"))
}
