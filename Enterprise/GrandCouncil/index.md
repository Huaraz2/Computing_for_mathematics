---
layout : page
title  : Grand Council
---

Here are the videos from past grand councils:

{% for year in site.data.grand_council %}
# {{year.year}}
    {% for talk in year.talks %}
1. [{{talk.company}}]({{talk.url}})
    {% endfor %}
{% endfor %}
