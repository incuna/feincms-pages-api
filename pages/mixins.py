class LinksMixin(object):
    links_fields = []

    def to_representation(self, obj):
        fields = super(LinksMixin, self).to_representation(obj)
        fields['links'] = {k: fields.pop(k) for k in self.links_fields if k in fields}
        return fields
