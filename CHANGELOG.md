# Changelog for feincms-pages-api

## 0.1.3

* Support `django-orderable` version `3`.

## 0.1.2

* Test against Django `1.7`
* Allow up to FeinCMS `1.10`.

## 0.1.1

* Use feincms-extensions `render_regions` which passes the request through to render

## 0.1.0

* Finish migrating changes from incuna internal pages app
    * Include domain in Group links
    * Rename query param slug -> group
    * Allow anonymous read-only access to Pages
    * Lookup Pages by slug, not pk
