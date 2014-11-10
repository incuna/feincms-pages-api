class LinksMixin(object):
    links_fields = []

    def to_native(self, obj):
        fields = super(LinksMixin, self).to_native(obj)
        fields['links'] = {k: fields.pop(k) for k in self.links_fields if k in fields}
        return fields
