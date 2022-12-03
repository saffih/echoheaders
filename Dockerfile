FROM python
ADD ./app app
WORKDIR /app
EXPOSE 8080
CMD ["python", "echo.py"]

