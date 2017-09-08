default: clean install copy zip

install: build_path
	pip install -r requirements.txt -t build

build_path:
	mkdir build

build_dist:
	mkdir dist

copy:
	cp -R src/* build/

zip: build_dist
	cd build && zip -r ../dist/lambda.zip .

clean:
	rm -rf build
	rm -rf dist
