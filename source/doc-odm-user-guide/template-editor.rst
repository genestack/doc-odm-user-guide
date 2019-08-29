Template Editor
###############

The Template Editor application allows to create, customize and update templates for data import.

How to access the application?
------------------------------

To get started use short-cut dock and select **Template Editor**.

.. image:: images/shortcuts-template-editor.png
   :scale: 45 %
   :align: center

On the application page you will see the available import templates. Also, you can find out by whom and when it was
created, updated. Click on the template name to explore it in more detail.

.. image:: images/templates-list.png
   :scale: 35 %
   :align: center



What is the import template?
----------------------------

Import templates contain metadata attributes that should be associated with a file being imported.
A separate template is created for each supported file type, namely "Study", "Sample", "Expression", "Variant"
and "Flow cytometry", and includes metadata fields that could be used in the subsequent curation process.


Regardless the filetype the import template includes the following metadata fields:

- *Name* — name of metadata filed that should be included in the metainfo (e.g. "Accession", "Organism");
- *Required* — determines whether the metadata field should be mandatory or not; if a field is marked as required
  and is left blanked or it is incorrectly filled in, it is highlighted in red;
- *Metainfo type* — indicates metadata type for the filed, namely text, integer, decimal, date, yes/no and external link;
- *Single* — indicates if several values can be added to a given field;
- *Read-only* — represents permissions for editing, where `yes` means that you cannot edit; the metadata
- *Dictionary* — allows to specify a dictionary providing standardized and unified terms that can be used in data
  curation and help to validate and harmonise metadata.


.. image:: images/template-example.png
   :scale: 75 %
   :align: center


Create and edit import template
-------------------------------

Click **Create copy** to make your own editable copy of a template and modify it if necessary.

.. image:: images/template-copy.png
   :align: center

Autocomplete can help you to specify an appropriate dictionary to be used in metadata validation in the Study Metainfo Editor.


.. image:: images/edit-template.png
   :align: center


Change import template
----------------------

By default data is imported with the **Default Import Template**, which includes metadata
columns along with associated dictionaries/ontologies. Feel free to change template before
importing data or in the **Study Metainfo Editor ODM** app when editing metadata:


1) To change a template for importing an Arvados project, you should open **Arvados Importer** app and
   click **Choose another**. All the available templates will be listed in the opening pop-up window.

.. image:: images/change-template-importer.png
   :scale: 65 %
   :align: center

Hover over the templates and explore them in the **Template Editor** app
if necessary by click **View in editor**. To change a template click its name.

.. image:: images/change-template-list.png
   :scale: 40 %
   :align: center

2) To change a template in the **Study Metainfo Editor ODM** app click **Choose another** on the app page and select
   the template of your interest in the list of suggested files.
   Click **View in editor** to open it  with Template Editor.

.. image:: images/change-template-me.png
   :scale: 65 %
   :align: center