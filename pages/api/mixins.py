class LinksMixin(object):
    links_fields = []

    def to_native(self, obj):
        fields = super(LinksMixin, self).to_native(obj)
        fields['links'] = {key: fields.pop(key) for key in self.links_fields if key in fields}
        return fields
