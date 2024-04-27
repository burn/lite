SHELL     := bash 
MAKEFLAGS += --warn-undefined-variables
TOP        = $(shell git rev-parse --show-toplevel)

.SILENT: 

help :  ## show help
	awk 'BEGIN               { FS = ":.*?## "; print "\nmake [WHAT]" } \
       /^[^[:space:]].*##/ { printf "   \033[36m%-10s\033[0m : %s\n", $$1, $$2} \
      ' $(MAKEFILE_LIST)

put: ## save this repos
	@read -p "commit msg> " x ;\
	y=$${x:-saved} ; \
	git commit -am "$$y" ; \
	git push --quiet; git status ; \
	echo "$$y: saved!"

pull: ## get updates from cloud
	git pull --quiet

../docs/%.html : %.py $(shell which pycco > /dev/null) ## python ==> doc
	mkdir -p ../docs
	pycco -d ../docs $^
	echo "p {text-align: right; }" >> ../docs/pycco.css
