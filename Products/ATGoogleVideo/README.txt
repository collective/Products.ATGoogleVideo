.. contents:: Table of Contents
   :depth: 2

Products.ATGoogleVideo
****************************************

Overview
--------

**Products.ATGoogleVideo** an Archetypes based product that adds a new content 
type to maintain references to videos stored in "Google 
Video":http://video.google.com/ or "YouTube":http://www.youtube.com/ into a
Plone site.

**Products.ATGoogleVideo** was initially developed as part of
"Julius":http://julius.jornada.com.mx/, a project to create a system for 
Newspaper Workflow Automation based on the requirements of La Jornada and on the 
"IPTC News Architecture":http://www.iptc.org/.

Requirements
------------

    - Plone 4.0.x (http://plone.org/products/plone)
    - Plone 3.0.x (http://plone.org/products/plone)

Screenshot
-----------

    .. image:: http://www.simplesconsultoria.com.br/tecnologia/plone/produtos/products.atgooglevideo/Products.ATGoogleVideo-0.9-screenshot.png/image_preview

Installation
------------
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``Products.ATGoogleVideo``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            Products.ATGoogleVideo

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the product (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource registries
in order to see the effects of the product installation.

Acknowlegements
---------------

This product could not be possible without the work of the following people:

   * Martin Aspeli for his "RichDocument: Creating content types the Plone 2.1
     way":http://plone.org/documentation/tutorial/richdocument tutorial
   
   * Andy McKay for his
     "book":http://plone.org/documentation/manual/definitive-guide and his 
     tutorial on "Testing and Development 
     Practices":http://plonebootcamps.com/courses/conf-adv
     
   * David Convent for his "DIY Plone 
     Style":http://plone.org/products/diyplonestyle product

Contributing
--------------

    Code repository can be found at `Plone Collective 
    <https://svn.plone.org/svn/collective/Products.ATGoogleVideo>`_


Credits
-------
   
   * Héctor Velarde <hvelarde@jornada.com.mx> (Original product)
    
   * `Simples Consultoria <http://www.simplesconsultoria.com.br/>`_ 
     (egg version)
    

