# Green Solar Energy — site build notes

The 19 HTML pages in the site root are **generated** from these three scripts. Editing a
generated `.html` file directly works, but the change is lost the next time the build runs —
prefer editing the source below and regenerating.

```bash
python _build/build.py
```

| File | What lives in it |
| --- | --- |
| `build_data.py` | All content: company details, the 12 services (copy, images, benefits, FAQs), why-choose cards, process steps, 12 testimonials, home FAQs, video list, gallery list |
| `build_parts.py` | Shared layout: `<head>`, topbar, navbar, mobile drawer, footer, floating side rail, and the reusable sections (why-choose, services, process, counters, videos, FAQ, testimonials, quote, map, CTA) |
| `build.py` | Page assembly — hero, about, PM Surya Ghar section, and one function per page type |

## Common edits

- **Company details** → `SITE` dict at the top of `build_data.py`
- **Add / change a service** → add an entry to `SERVICES` in `build_data.py`; an inner page
  `service-<slug>.html` is generated automatically and the slug is added to every menu and footer
- **Social media links** → `SOCIALS` in `build_parts.py` (currently placeholder profile URLs —
  replace with the real Facebook / Instagram / YouTube / LinkedIn pages)
- **Colours / spacing / components** → `assets/css/main.css` (all design tokens are CSS variables
  in the `:root` block, derived from the company logo)
- **Behaviour** (slider, marquees, FAQ, video mute, lightbox, forms) → `assets/js/site.js`

## Forms

There is no server behind the site, so both forms (Request a Quote, Apply for Subsidy) package
the entered fields and hand them to WhatsApp on `+91 74411 76223`, then show a confirmation.
To switch to email or a CRM later, replace the `form[data-ajax]` submit handler at the bottom of
`assets/js/site.js` with a normal `fetch()` POST.

## Archived template files

`_removed-pages/` holds everything from the original purchased template that the new site no longer
uses — the removed pages (blog, service-2, privacy, terms, coming-soon) and the unused template CSS,
JS and images. Nothing in the live site references it; the folder can be deleted once you are happy.
