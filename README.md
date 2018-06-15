# mitsuba_tools

Some useful tools for Mitsuba.

### rm_instance

* Convert `instance` and `shapegroup` shapes into non-instanced shapes.
* Usually used for Blender exported Mitsuba scenes which may contain `instance` and `shapegroup` shapes.

### rm_twosided

* Remove the `twosided` attributes of BSDFs.
* To check the models' surface normal by rendering the normal channel, the `twosided` attributes must be removed.
