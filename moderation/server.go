package main

import (
	"log"
	"net/http"

	"github.com/labstack/echo/v4"
)

type EventType struct {
	Type string `json:"name"`
}

func receiveEvent(c echo.Context) error {
	e := new(EventType)
	if err := c.Bind(e); err != nil {
		return err
	}

	log.Print(e.Type)

	return c.NoContent((http.StatusOK))
}

func main() {
	e := echo.New()

	e.POST("/events", receiveEvent)

	e.Logger.Fatal(e.Start(":5003"))
}
