Workplace Notify Step `Docker Repository on hub.docker`_
=========================================================

Posts wercker build/deploy status to a `Workplace Groups`_

:Version: 0.0.0
:Web: https://github.com/labpositiva/step-pretty-workplace-notify
:Download: https://github.com/labpositiva/step-pretty-workplace-notify
:Source: https://github.com/labpositiva/step-pretty-workplace-notify
:Keywords: step, wercker

.. contents:: Table of Contents:
    :local:

Requirements
************

.. code-block::

   $ make setup

Options
=======

-  ``token`` - Token Api Facebook.
-  ``group-id`` - Group id de Facebook.
-  ``branches`` - Specific branches to notify. (regular expression)
-  ``notify_on`` - Allows you to specify to notify on ``passed`` or
   ``failed``. (default all allows notify)
-  ``formatting`` - MARKDOWN
-  ``passed_message``/``failed_message`` - Allows you to define
   additional message on ``passed``/``failed``.

Developing
**********

Setup
=====

.. code-block:: bash

  λ cat .env-sample > .env
  λ make setup
  λ make build
  λ make up


Environment
===========

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Key
     - Value
   * - Key
     - Value

How To Use
**********

posts build notification

Build
=====

.. code:: yml

    build:
        after-steps:
            - labpositiva/pretty-workplace-notify:
                group_id: $WORKPLACE_GROUP_ID
                token: $WORKPLACE_TOKEN

notify on specific branches only

.. code:: yml

    build:
        after-steps:
            - labpositiva/pretty-workplace-notify:
                group_id: $WORKPLACE_GROUP_ID
                token: $WORKPLACE_TOKEN
                branches: ^master$

notify on failed build only

.. code:: yml

    build:
        after-steps:
            - labpositiva/pretty-workplace-notify:
                group_id: $WORKPLACE_GROUP_ID
                token: $WORKPLACE_TOKEN
                notify_on: "failed"

define additional message on passed build

.. code:: yml

    build:
        after-steps:
            - labpositiva/pretty-workplace-notify:
                group_id: $WORKPLACE_GROUP_ID
                token: $WORKPLACE_TOKEN
                passed_message: yay :smile:

Deploy
======

posts deploy notification

.. code:: yml

    deploy:
        after-steps:
            - labpositiva/pretty-workplace-notify:
                group_id: $WORKPLACE_GROUP_ID
                token: $WORKPLACE_TOKEN

Others
------

Other commands for developing are written in Makefile:

.. code-block:: bash

  λ make
    ༼ つ ◕_◕ ༽つ Commands
      build                Build docker container by env
      clean                clean Files compiled
      documentation        Make Documentation
      down                 remove containers docker by env
      environment          Make environment for developer
      install              Install with var env Dependences
      list                 List of current active services by env
      lint                 Clean files unnecesary
      test                 make test
      up                   Up application by env
      restart              Reload services
      ssh                  Connect to container
      stop                 stop containers docker by env
      setup                Install dependences initial
      verify_network       Verify network
      help                 Show help text

Changelog
*********

Please see `changelog`_ for more information what has changed recently.

Contributing
************

Please see `contributing`_ for details.

Credits
*******

Made with :heart: :coffee:️and :pizza: by `company`_.

..  links:

.. _`author`: https://github.com/luismayta
.. _`changelog`: CHANGELOG.rst
.. _`contributors`: AUTHORS
.. _`contributing`: CONTRIBUTING.rst
.. _Docker Repository on hub.docker: https://hub.docker.com/
.. _`company`: https://github.com/labpositiva
.. _Workplace Groups: https://developers.facebook.com/docs/workplace/integrations/custom-integrations/reference/group