# BonfireNightUK.co.uk — MVP Decision Lock

**Last Updated:** 2026-02-20  
**Status:** 🔒 Locked Before Build

---

## Purpose

These 9 decisions define the complete scope, structure, and constraints of the MVP.

**Rule:** Nothing gets built until these are answered and locked.

**Why:** Prevents feature creep, protects timeline, ensures 2027 reusability, and maximises ROI on build credits.

---

## ✅ 1️⃣ Exact Scope Lock (No Feature Creep)

### Public Side — MVP ONLY

- [ ] Homepage
- [ ] City page template (SEO engine)
- [ ] Event detail template
- [ ] Safety + legal content hub (4-5 static pages)
- [ ] Postcode search (find nearest city)
- [ ] Email capture by postcode (annual reminder list)

### Organiser Side — MVP ONLY

- [ ] Account creation (email + password)
- [ ] Create event form
- [ ] Upload event details + image
- [ ] Free listing (default)
- [ ] Upgrade to Featured (one-time payment)
- [ ] Stripe payment integration
- [ ] Automatic event expiry (November 6)
- [ ] Automatic renewal reminder email (August 1 next year)

### EXPLICITLY EXCLUDED FROM MVP

- ❌ Dashboards
- ❌ Analytics for organisers
- ❌ Ratings or reviews
- ❌ Chatbots
- ❌ Community features
- ❌ Social media feeds
- ❌ Newsletter system
- ❌ Ticketing integration

**Decision:**  
☐ Locked  
☐ Needs revision

---

## ✅ 2️⃣ Monetisation Model Finalised

### Revenue Streams (MVP)

1. **Featured listings** (primary revenue)
2. **Affiliate links** (firework retailers, pet calming products)
3. **Google Ads** (optional, low priority)

### NOT Included

- ❌ Ticketing system
- ❌ Subscription model
- ❌ Premium dashboards
- ❌ Pay-per-click event promotions

### Featured Listing Pricing

**Range:** £99–£199  
**Default for 2026:** £149  

**Decision:**  
☐ Pricing locked at £149  
☐ Alternative pricing: £___

---

## ✅ 3️⃣ Information Architecture (SEO Engine)

### URL Structure

**Homepage:**  
`/`

**City pages (SEO growth engine):**  
`/manchester-bonfire-night-2026`  
`/london-bonfire-night-2026`  
`/birmingham-bonfire-night-2026`  
etc.

**Event pages:**  
`/events/manchester-city-centre-fireworks-2026`  
`/events/[slug]-[year]`

**Safety Hub (Authority Content):**  
`/firework-laws-uk`  
`/firework-curfew-times`  
`/firework-categories-f1-f4`  
`/bonfire-night-pet-safety`

### City Coverage

**Question:** How many UK cities to include in MVP?

- [ ] Top 20 cities
- [ ] Top 50 cities
- [ ] Top 100 cities
- [ ] All UK cities with population >50k
- [ ] Other: ___________

**Decision:**  
☐ City count locked  
☐ Generation approach defined (pre-generate vs dynamic)

---

## ✅ 4️⃣ Database Structure (Season-Proof)

### Required Tables

**Users:**
- id
- email
- password_hash
- created_at

**Events:**
- id
- user_id (organiser)
- city_id
- title
- description
- date
- time
- location (address)
- latitude / longitude
- ticket_url
- image_url
- featured (boolean)
- status (active / expired)
- year (2026, 2027, etc.)
- expires_at (datetime, default: Nov 6)
- created_at
- updated_at

**Cities:**
- id
- name
- slug (e.g., "manchester")
- latitude / longitude
- region
- created_at

**Payments:**
- id
- user_id
- event_id
- stripe_payment_id
- amount (pence)
- currency (GBP)
- status (pending / succeeded / failed)
- created_at

**Email Subscribers:**
- id
- email
- postcode
- city_id (nullable, derived from postcode)
- subscribed_at
- unsubscribed_at (nullable)

### Additional Fields Needed?

**Decision:**  
☐ Schema locked  
☐ Additional fields required: ___________

---

## ✅ 5️⃣ Automation Logic Defined

### Automated Behaviours (MVP)

1. **Event Expiry:**  
   - All events automatically expire on **November 6** (year defined in event record)  
   - Status changes to "expired" automatically  
   - Expired events hidden from public listings

2. **Renewal Reminders:**  
   - On **August 1** each year, send automated email to organisers with expired events  
   - Email includes link to duplicate/renew event for upcoming season

3. **Email List Activation:**  
   - On **August 1** each year, send "Events are now live for 2027" email to subscribers  
   - Segmented by city (based on postcode)

### Moderation

- **MVP:** No manual moderation  
- Events go live immediately on submission

**Decision:**  
☐ Automation logic locked  
☐ Changes needed: ___________

---

## ✅ 6️⃣ Homepage Hierarchy

### Above-the-Fold Order (Top to Bottom)

1. **Headline:**  
   "Find Bonfire Night Events Near You"

2. **Postcode Search Bar**  
   (Single input, button: "Find Events")

3. **Major City Quick Links**  
   (e.g., London, Manchester, Birmingham, Leeds, Glasgow, Edinburgh, Bristol, etc.)

4. **Email Capture Form**  
   "Get notified when 2027 events go live near you"  
   (Email + Postcode inputs)

5. **Safety Credibility Section**  
   (Brief intro + links to firework laws, curfew times, pet safety)

6. **CTA: "Submit Your Event"**  
   (Button, links to organiser sign-up)

### NOT Included on Homepage

- ❌ Blog previews
- ❌ Social media feeds
- ❌ Testimonials
- ❌ Recent events list
- ❌ Featured organisers

**Decision:**  
☐ Homepage hierarchy locked  
☐ Changes needed: ___________

---

## ✅ 7️⃣ Brand Positioning Locked

### Brand Statement

> "The trusted UK guide to Bonfire Night events."

### Tone & Attributes

- **British** (not American)
- **Established** (not startup-y)
- **Trustworthy** (credible, safe)
- **Clean** (minimal, professional)
- **Not childish** (no playful illustrations or gamification)
- **Not gimmicky** (no hype, no tech-bro language)

### Visual Identity

**Colour Palette:**  
- Navy (primary)
- Deep red (accent)
- Off-white (background)

**Typography:**  
- Clean, readable, professional
- Not decorative or playful

**Imagery:**  
- Real fireworks photos
- No cartoons or illustrations (unless necessary for icons)

**Decision:**  
☐ Brand positioning locked  
☐ Changes needed: ___________

---

## ✅ 8️⃣ 2027 Reuse Model

### Question: How do organisers renew events each year?

**Option A: Manual Re-creation**  
Organisers log in and manually create a new event each year, copying details themselves.

**Option B: Auto-Clone Draft**  
System automatically creates a draft copy of last year's event on August 1.  
Organisers log in, review, update date/details, and republish.

**Option C: One-Click Renewal**  
Organisers receive email with "Renew Last Year's Event" button.  
Click → Pre-filled form → Edit → Publish.

**Recommended:** Option C (lowest friction, highest renewal rate)

**Decision:**  
☐ Renewal model locked  
☐ Chosen option: ___________

---

## ✅ 9️⃣ Phase Timeline Commitment

### MVP Build Timeline (Feb–Sept 2026)

**Phase 1: Foundation (Feb–March)**  
- Database design
- Core site structure
- City page template

**Phase 2: Public Site (April–May)**  
- Homepage
- Event listings
- City pages
- Postcode search

**Phase 3: Organiser + Payments (June)**  
- Account creation
- Event submission
- Featured upgrade (Stripe)

**Phase 4: SEO Content (July)**  
- Safety Hub pages
- City page SEO optimisation
- Schema markup

**Phase 5: Outreach (August)**  
- Organiser outreach
- Email list priming
- Press/influencer outreach

**Phase 6: Peak Season (Sept–Nov)**  
- Live operation
- Minimal intervention
- Revenue tracking

**Commitment:**  
☐ Timeline locked  
☐ Adjustments needed: ___________

---

## 🎯 Build Authority Checkpoint

**These 9 decisions must be locked before build begins.**

**Why:**  
- Protects timeline  
- Prevents feature creep  
- Ensures 2027 reusability  
- Maximises build credit ROI  
- Creates a boring, repeatable, high-leverage system

**When locked:**  
Build becomes fast, clean, and predictable.

**When skipped:**  
Rebuild in 2027, scope creep, missed deadlines, wasted credits.

---

## Sign-Off

**Decision Authority:** Paul Hooper  
**Locked Date:** [ TBD ]

**Next Step:** Review this document, answer all ☐ checkboxes, lock decisions, then proceed to tech stack selection.
