BIN = fortuna
PROTO_DIR = proto

run: generate
	python proto_test.py

generate:
	protoc -I${BIN}/${PROTO_DIR} --python_out=${BIN}/${PROTO_DIR} ${BIN}/${PROTO_DIR}/*.proto

clean:
	rm ${BIN}/${PROTO_DIR}/*_pb2.py