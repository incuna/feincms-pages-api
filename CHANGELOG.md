# Changelog for feincms-pages-api

# Upcoming

* Update test_requirements

## 1.3.0

* Add `djangorestframework` v3.3 support
* Add support for Django 1.8.
* Drop support for Django 1.6.

## 1.2.0

* Add `djangorestframework` v3.2 support

Notes:
* `request.QUERY_PARAMS` has been deprecated for `request.query_params`
* add `view_name` to `extra_kwargs['url']`

## 1.1.0

* Support rendering `Page` content types as `json`. (Merge `0.2.0`)

## 1.0.0

* Add django-rest-framework v3 support.
* Remove django-rest-framework v2 support.

## 0.2.0

* Support rendering `Page` content types as `json`.

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
