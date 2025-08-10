#!/bin/bash
cd /home/mostefa/Development/Divers/eskalate/backend
uvicorn app.main:app --reload --port 8000
