image = album/gymx

proto:
	python3 -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. gymx/*.proto

dist:
	python3 setup.py sdist

upload:
	twine upload dist/*

clean:
	rm -r dist *.egg-info

release: dist upload clean

build:
	docker build -t $(image) .

run:
	docker run -p 54321:54321 $(image)

push:
	docker push $(image)
