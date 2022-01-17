==============
pytest-alt-vrt
==============

A simple plugin for Visual Regression Testing of Altair charts to use with pytest. Adapted from the `Automating Visual Regression Tests with Python and Selenium`_ blog post by U. Rinat.

----

This `pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `cookiecutter-pytest-plugin`_ template.


License
-------

Distributed under the terms of the `MIT`_ license, ``pytest-alt-vrt`` is free and open source software.


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.


Notes
-----

- `Selenium WebDriver API`_ documentation.
- ``pytest --driver Chrome``
- ``pytest --driver Chrome --alt-vrt-save-baseline``
- Print: ``pytest --driver Chrome -s``
- ``pipenv install --python 3.6``
- `Displaying Altair Charts`_ documentation.
- `nbdime`_ package.
- `Register entry point hooks for things like pytest/click etc.`_ Poetry issue.
- `pixelmatch`_ and `pixelmatch-py`_ packages.
- `playwright-pytest`_ and `pytest-playwright-snapshot`_ plugins. 
- `[Feature]: Visual comparisons in python`_ and `[FEATURE] Add support for visual regression / snapshot testing`_ (open) issues.


.. _`Automating Visual Regression Tests with Python and Selenium`: https://blog.rinatussenov.com/automating-manual-visual-regression-tests-with-python-and-selenium-be66be950196
.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/joaopalmeiro/pytest-alt-vrt/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`Selenium WebDriver API`: https://selenium-python.readthedocs.io/api.html
.. _`Displaying Altair Charts`: https://altair-viz.github.io/user_guide/display_frontends.html
.. _`nbdime`: https://github.com/jupyter/nbdime
.. _`Register entry point hooks for things like pytest/click etc.`: https://github.com/python-poetry/poetry/issues/1641#issuecomment-559502420
.. _`pixelmatch`: https://github.com/mapbox/pixelmatch
.. _`pixelmatch-py`: https://github.com/whtsky/pixelmatch-py
.. _`playwright-pytest`: https://github.com/microsoft/playwright-pytest
.. _`pytest-playwright-snapshot`: https://github.com/kumaraditya303/pytest-playwright-snapshot
.. _`[Feature]: Visual comparisons in python`: https://github.com/microsoft/playwright-python/issues/837
.. _`[FEATURE] Add support for visual regression / snapshot testing`: https://github.com/microsoft/playwright-pytest/issues/63
