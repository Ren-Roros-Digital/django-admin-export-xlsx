Django Admin Export xlsx
========================

| All credit goes to the autor of 
| https://www.djangosnippets.org/snippets/10681/

Usage
-----

| https://docs.djangoproject.com/en/dev/ref/contrib/admin/actions/

.. code:: python

        from export_xlsx import export_as_xls

        class <arbitraryAdminClass>(admin.ModelAdmin):
            ...
            actions [export_as_xls]
