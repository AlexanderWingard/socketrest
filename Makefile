VERSION=1.6.4
ENV=env
URL_BASE=https://pypi.python.org/packages/source/v/virtualenv

.PHONY: run

run: $(ENV)/bin/python
	$(ENV)/bin/python server.py

$(ENV)/bin/python: requirements.txt
	curl -O $(URL_BASE)/virtualenv-$(VERSION).tar.gz
	tar xzf virtualenv-$(VERSION).tar.gz
	python virtualenv-$(VERSION)/virtualenv.py --no-site-packages $(ENV)
	rm -rf virtualenv-$(VERSION) virtualenv-$(VERSION).tar.gz
	$(ENV)/bin/pip install -r requirements.txt
