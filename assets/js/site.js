/* Green Solar Energy — site scripts (vanilla JS, no dependencies) */
(function () {
    'use strict';

    /* ---------- Mobile menu ---------- */
    var drawer = document.getElementById('mobileMenu');
    var overlay = document.getElementById('overlay');
    function closeDrawer() {
        if (drawer) drawer.classList.remove('open');
        if (overlay) overlay.classList.remove('show');
        document.body.style.overflow = '';
    }
    document.querySelectorAll('[data-menu-open]').forEach(function (b) {
        b.addEventListener('click', function () {
            drawer.classList.add('open');
            overlay.classList.add('show');
            document.body.style.overflow = 'hidden';
        });
    });
    document.querySelectorAll('[data-menu-close]').forEach(function (b) {
        b.addEventListener('click', closeDrawer);
    });
    if (overlay) overlay.addEventListener('click', closeDrawer);

    document.querySelectorAll('.mm-list .sub-toggle').forEach(function (t) {
        t.addEventListener('click', function (e) {
            e.preventDefault();
            var sub = t.parentElement.querySelector('.mm-sub');
            if (sub) sub.classList.toggle('open');
        });
    });

    /* ---------- Sticky header ---------- */
    var nav = document.querySelector('.navbar');
    if (nav) {
        var navTop = nav.offsetTop;
        var spacer = document.createElement('div');
        window.addEventListener('scroll', function () {
            if (window.scrollY > navTop + 40) {
                if (!nav.classList.contains('is-stuck')) {
                    nav.classList.add('is-stuck');
                    spacer.style.height = nav.offsetHeight + 'px';
                    nav.parentNode.insertBefore(spacer, nav);
                }
            } else if (nav.classList.contains('is-stuck')) {
                nav.classList.remove('is-stuck');
                if (spacer.parentNode) spacer.parentNode.removeChild(spacer);
            }
        }, { passive: true });
    }

    /* ---------- Hero video ---------- */
    var heroVideo = document.querySelector('.hero-video');
    if (heroVideo) {
        heroVideo.muted = true;
        var hp = heroVideo.play();
        if (hp && hp.catch) hp.catch(function () { });
    }

    /* ---------- Scroll reveal ---------- */
    var revealEls = document.querySelectorAll('.reveal');
    if ('IntersectionObserver' in window && revealEls.length) {
        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
            });
        }, { threshold: 0.12 });
        revealEls.forEach(function (el) { io.observe(el); });
    } else {
        revealEls.forEach(function (el) { el.classList.add('in'); });
    }

    /* ---------- Counters ---------- */
    var counters = document.querySelectorAll('[data-count]');
    if (counters.length && 'IntersectionObserver' in window) {
        var cio = new IntersectionObserver(function (entries) {
            entries.forEach(function (en) {
                if (!en.isIntersecting) return;
                var el = en.target, target = parseFloat(el.getAttribute('data-count')), t0 = null;
                function step(ts) {
                    if (!t0) t0 = ts;
                    var p = Math.min((ts - t0) / 1600, 1);
                    el.textContent = Math.floor(target * (1 - Math.pow(1 - p, 3))).toLocaleString('en-IN');
                    if (p < 1) requestAnimationFrame(step);
                }
                requestAnimationFrame(step);
                cio.unobserve(el);
            });
        }, { threshold: 0.4 });
        counters.forEach(function (c) { cio.observe(c); });
    }

    /* ---------- FAQ accordion ---------- */
    document.querySelectorAll('.faq-q').forEach(function (q) {
        q.addEventListener('click', function () {
            var item = q.closest('.faq-item');
            var body = item.querySelector('.faq-a');
            var isOpen = item.classList.contains('open');
            var group = item.parentElement;
            group.querySelectorAll('.faq-item.open').forEach(function (o) {
                o.classList.remove('open');
                o.querySelector('.faq-a').style.maxHeight = null;
            });
            if (!isOpen) {
                item.classList.add('open');
                body.style.maxHeight = body.scrollHeight + 'px';
            }
        });
    });
    document.querySelectorAll('.faq-item.open').forEach(function (o) {
        var b = o.querySelector('.faq-a');
        if (b) b.style.maxHeight = b.scrollHeight + 'px';
    });

    /* ---------- Video sound toggles ---------- */
    document.querySelectorAll('.video-card').forEach(function (card) {
        var vid = card.querySelector('video');
        var btn = card.querySelector('.v-sound');
        if (!vid || !btn) return;
        vid.muted = true;
        var play = vid.play();
        if (play && play.catch) play.catch(function () { });
        btn.addEventListener('click', function () {
            if (vid.muted) {
                // only one video with sound at a time
                document.querySelectorAll('.video-card video').forEach(function (v) {
                    if (v !== vid) {
                        v.muted = true;
                        var ob = v.closest('.video-card').querySelector('.v-sound i');
                        if (ob) ob.className = 'fas fa-volume-xmark';
                    }
                });
                vid.muted = false;
                btn.querySelector('i').className = 'fas fa-volume-high';
                btn.setAttribute('aria-label', 'Mute video');
            } else {
                vid.muted = true;
                btn.querySelector('i').className = 'fas fa-volume-xmark';
                btn.setAttribute('aria-label', 'Unmute video');
            }
        });
    });

    /* ---------- Gallery filter + lightbox ---------- */
    var filterBtns = document.querySelectorAll('.gal-filter button');
    filterBtns.forEach(function (b) {
        b.addEventListener('click', function () {
            filterBtns.forEach(function (x) { x.classList.remove('active'); });
            b.classList.add('active');
            var f = b.getAttribute('data-filter');
            document.querySelectorAll('.gal-item').forEach(function (it) {
                var show = f === '*' || it.getAttribute('data-cat') === f;
                it.style.display = show ? '' : 'none';
            });
        });
    });

    var lb = document.getElementById('lightbox');
    if (lb) {
        var lbImg = lb.querySelector('img');
        var items = [], current = 0;
        function refresh() {
            items = Array.prototype.filter.call(
                document.querySelectorAll('.gal-item'),
                function (i) { return i.style.display !== 'none'; }
            );
        }
        function show(i) {
            refresh();
            if (!items.length) return;
            current = (i + items.length) % items.length;
            var src = items[current].getAttribute('data-full') || items[current].querySelector('img').src;
            lbImg.src = src;
            lb.classList.add('open');
            document.body.style.overflow = 'hidden';
        }
        document.querySelectorAll('.gal-item').forEach(function (it) {
            it.addEventListener('click', function () {
                refresh();
                show(items.indexOf(it));
            });
        });
        lb.querySelector('.lb-close').addEventListener('click', function () {
            lb.classList.remove('open');
            document.body.style.overflow = '';
        });
        lb.querySelector('.lb-prev').addEventListener('click', function (e) { e.stopPropagation(); show(current - 1); });
        lb.querySelector('.lb-next').addEventListener('click', function (e) { e.stopPropagation(); show(current + 1); });
        lb.addEventListener('click', function (e) {
            if (e.target === lb) { lb.classList.remove('open'); document.body.style.overflow = ''; }
        });
        document.addEventListener('keydown', function (e) {
            if (!lb.classList.contains('open')) return;
            if (e.key === 'Escape') { lb.classList.remove('open'); document.body.style.overflow = ''; }
            if (e.key === 'ArrowLeft') show(current - 1);
            if (e.key === 'ArrowRight') show(current + 1);
        });
    }

    /* ---------- Scroll to top ---------- */
    var st = document.querySelector('.scroll-top');
    if (st) {
        window.addEventListener('scroll', function () {
            st.classList.toggle('show', window.scrollY > 500);
        }, { passive: true });
        st.addEventListener('click', function () { window.scrollTo({ top: 0, behavior: 'smooth' }); });
    }

    /* ---------- Repeatable phone-number field (max 4) ---------- */
    document.querySelectorAll('[data-phone-repeater]').forEach(function (box) {
        var list = box.querySelector('.phone-list');
        var addBtn = box.querySelector('.phone-add');
        var max = parseInt(box.getAttribute('data-max') || '4', 10);

        function sync() {
            var rows = list.querySelectorAll('.phone-row');
            addBtn.hidden = rows.length >= max;
            rows.forEach(function (r, i) {
                var rm = r.querySelector('.phone-remove');
                if (rm) rm.hidden = i === 0;
            });
        }
        addBtn.addEventListener('click', function () {
            var rows = list.querySelectorAll('.phone-row');
            if (rows.length >= max) return;
            var row = document.createElement('div');
            row.className = 'phone-row';
            row.innerHTML = '<input type="tel" name="phone' + (rows.length + 1) +
                '" pattern="[0-9+ ]{10,15}" placeholder="Alternate mobile number">' +
                '<button type="button" class="phone-remove" aria-label="Remove this number"><i class="fas fa-xmark"></i></button>';
            list.appendChild(row);
            row.querySelector('input').focus();
            sync();
        });
        list.addEventListener('click', function (e) {
            var rm = e.target.closest('.phone-remove');
            if (!rm) return;
            rm.closest('.phone-row').remove();
            sync();
        });
        sync();
    });

    /* ---------- Forms ----------
       No backend: every enquiry is packaged into a mailto: link addressed to
       the company inbox with the submitted fields pre-filled in the body,
       then handed to the visitor's own default email client so they can
       review it and press Send themselves. Replace with a real POST to a
       backend/mailer later if one is added — everything else (validation,
       success/error messaging) can stay as is. */
    var CONTACT_EMAIL = 'Greenenergyconsultant2018@gmail.com';
    var MAILTO_SAFE_LENGTH = 1800; // conservative cross-client mailto: URL budget

    function fieldLabel(form, el) {
        if (el.id) {
            var lab = form.querySelector('label[for="' + el.id + '"]');
            if (lab) return lab.textContent.replace(/\s*\(.*?\)\s*/g, '').trim();
        }
        var repeat = /^phone(\d+)$/.exec(el.name || '');
        if (repeat) return 'Mobile Number ' + repeat[1];
        return el.name ? el.name.charAt(0).toUpperCase() + el.name.slice(1) : 'Field';
    }

    document.querySelectorAll('form[data-ajax]').forEach(function (f) {
        var msg = f.querySelector('.form-msg');

        function showMsg(isError, html) {
            if (!msg) return;
            msg.innerHTML = html;
            msg.classList.toggle('is-error', !!isError);
            msg.classList.add('show');
            clearTimeout(msg._hideTimer);
            msg._hideTimer = setTimeout(function () { msg.classList.remove('show'); }, 16000);
        }

        f.addEventListener('submit', function (e) {
            e.preventDefault();

            /* ---- validation: native constraints (required / type=email / pattern) ---- */
            if (!f.checkValidity()) {
                f.reportValidity();
                return;
            }

            var fields = Array.prototype.slice.call(f.querySelectorAll('input[name], select[name], textarea[name]'));
            var filled = fields.filter(function (el) { return el.value && el.value.trim(); });
            if (!filled.length) {
                showMsg(true, 'Please fill in at least your name and mobile number before sending.');
                return;
            }

            var subjectBase = f.getAttribute('data-subject') || 'Website Enquiry';
            var nameField = f.querySelector('[name="name"]');
            var subject = subjectBase + (nameField && nameField.value ? ' — ' + nameField.value.trim() : '') + ' | Green Solar Energy Website';

            var lines = ['New ' + subjectBase + ' from the Green Solar Energy website:', ''];
            filled.forEach(function (el) { lines.push(fieldLabel(f, el) + ': ' + el.value.trim()); });
            var body = lines.join('\r\n');

            function buildMailto(b) {
                return 'mailto:' + CONTACT_EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(b);
            }

            var mailto = buildMailto(body);

            /* ---- guard against mail clients that silently drop overlong mailto: links ---- */
            if (mailto.length > MAILTO_SAFE_LENGTH) {
                var note = '\r\n\r\n(Message shortened for email compatibility.)';
                while (mailto.length > MAILTO_SAFE_LENGTH && body.length > 20) {
                    body = body.slice(0, -20);
                    mailto = buildMailto(body + note);
                }
                mailto = buildMailto(body + note);
            }

            try {
                window.location.href = mailto;
                showMsg(false,
                    'Thank you! Your email app should now open with this enquiry ready to send — please review it and click <strong>Send</strong>. ' +
                    'If nothing opened, <a href="' + mailto + '">click here to email us directly</a>, or write to us at ' +
                    '<a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a>.'
                );
                f.reset();
            } catch (err) {
                showMsg(true,
                    'We could not open your email app automatically. Please email us directly at ' +
                    '<a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + '</a> or call ' +
                    '<a href="tel:+917441176223">+91 74411 76223</a>.'
                );
            }
        });
    });

    /* ---------- Marquee duplication (seamless infinite loop) ---------- */
    document.querySelectorAll('.marquee-track').forEach(function (track) {
        if (track.getAttribute('data-cloned')) return;
        track.innerHTML += track.innerHTML;
        track.setAttribute('data-cloned', '1');
    });
})();
