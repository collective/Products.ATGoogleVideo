#!/bin/sh

PRODUCTNAME='atgooglevideo'
I18NDOMAIN='atgooglevideo'

# Synchronise the .pot with the templates.
i18ndude rebuild-pot --pot i18n/${PRODUCTNAME}.pot --create ${I18NDOMAIN} .
 	
# Synchronise the resulting .pot with the .po files
i18ndude sync --pot i18n/${PRODUCTNAME}.pot i18n/${PRODUCTNAME}-eu.po
i18ndude sync --pot i18n/${PRODUCTNAME}.pot i18n/${PRODUCTNAME}-es.po
i18ndude sync --pot i18n/${PRODUCTNAME}.pot i18n/${PRODUCTNAME}-el.po
i18ndude sync --pot i18n/${PRODUCTNAME}.pot i18n/${PRODUCTNAME}-it.po
i18ndude sync --pot i18n/${PRODUCTNAME}.pot i18n/${PRODUCTNAME}-pt-br.po
