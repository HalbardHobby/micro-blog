package main

import (
	"bytes"
	"encoding/json"
	"io"
	"log"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

var event_history = make([]json.RawMessage, 0)

func receiveEvent(c echo.Context) error {
	b, err := io.ReadAll(c.Request().Body)
	if err != nil {
		log.Fatalln(err)
	}
	log.Print(string(b))
	defer fanoutEvent(b)
	event_history = append(event_history, b)

	return c.NoContent(http.StatusOK)
}

func getEventHistory(c echo.Context) error {
	// json_history, _ := json.Marshal(event_history)
	return c.JSON(http.StatusOK, event_history[:])
}

func fanoutEvent(event []byte) {
	log.Print(string(event))

	_, err := http.Post("http://posts-cluster-service:5000/events/", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
	_, err = http.Post("http://comments-cluster-service:5000/events/", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
	_, err = http.Post("http://query-cluster-service:5000/events/", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
	_, err = http.Post("http://mod-service:5003/events/", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
}

func main() {
	e := echo.New()
	e.Use(middleware.CORS())

	e.GET("/events/", getEventHistory)
	e.POST("/events/", receiveEvent)

	e.Logger.Fatal(e.Start(":4999"))
}
