package main

import (
	"bytes"
	"io"
	"log"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func receiveEvent(c echo.Context) error {
	b, err := io.ReadAll(c.Request().Body)
	if err != nil {
		log.Fatalln(err)
	}
	defer fanoutEvent(b)

	return c.NoContent(http.StatusOK)
}

func fanoutEvent(event []byte) {
	_, err := http.Post("http://localhost:5000/events", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
	_, err = http.Post("http://localhost:5001/events", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
	_, err = http.Post("http://localhost:5002/events", "application/json", bytes.NewBuffer(event))
	if err != nil {
		log.Print(err)
	}
}

func main() {
	e := echo.New()
	e.Use(middleware.CORS())

	e.POST("/", receiveEvent)

	e.Logger.Fatal(e.Start(":4999"))
}
