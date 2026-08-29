import re

def update_html():
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Update Title and meta description
    html = re.sub(r'<title>.*?</title>', '<title>KNC Logistics Services</title>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<meta name="description"\s+content=".*?">', '<meta name="description"\n    content="KNC Logistics Services - A company delivering strategic business solutions.">', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 2. Update Header Logo Text
    html = re.sub(r'<span class="logo-main-name"[^>]*>.*?</span>', '<span class="logo-main-name"\n            style="font-family: \'Fraunces\', serif; font-weight: 700; font-size: 1.15rem; color: var(--navy); letter-spacing: 0.04em; white-space: nowrap; transition: font-size var(--tr);">KNC Logistics Services</span>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<span class="logo-sub"[^>]*>.*?</span>\s*</span>\s*<span class="logo-tagline"', '<span class="logo-tagline"', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<span class="logo-tagline"[^>]*>.*?</span>', '<span class="logo-tagline"\n            style="font-family: \'Space Grotesk\', sans-serif; font-size: 0.5rem; letter-spacing: 0.2em; text-transform: uppercase; color: var(--navy); opacity: 0.6; white-space: nowrap; transition: opacity var(--tr);">Strategic Business Solutions</span>', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Header links update - remove "KNC Logistics" from the header as it is now this page itself
    html = re.sub(r'<a href="knc-logistics\.html">.*?</a>', '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 3. Update Hero section
    html = re.sub(r'<h1>Connecting <em>purpose</em><br>with progress.</h1>', '<h1>Strategic <em>business</em><br>solutions.</h1>', html, flags=re.IGNORECASE)
    html = re.sub(r'<p class="lede"><mark>Mastery &amp; Precise Business House</mark> is a multidisciplinary consulting\s*organization helping\s*businesses achieve sustainable growth through strategic advisory, operational excellence, digital\s*transformation, and professional development.</p>', '<p class="lede"><mark>KNC Logistics Services</mark> delivers strategic business solutions. We are committed to delivering innovative, reliable, and value-driven business solutions that empower organizations to achieve operational excellence and sustainable growth.</p>', html, flags=re.IGNORECASE | re.DOTALL)
    
    # Remove Marquee as it mentions unsupported things like EdTech
    html = re.sub(r'<!-- MARQUEE -->.*?<!-- WHO WE ARE -->', '<!-- WHO WE ARE -->', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 4. Update "Who We Are"
    who_we_are_html = '''
    <div class="who-grid">
        <div class="reveal-left">
          <div class="who-img-wrap">
            <img src="images/about_team.png" alt="KNC Logistics Team"
              loading="lazy">
            <div class="who-img-badge">
              <strong>2026</strong>
              <span>Est. &middot; Riyadh, KSA</span>
            </div>
          </div>
        </div>
        <div class="who-text reveal-right">
          <span class="eyebrow">Who We Are?</span>
          <h2 style="font-size:clamp(2rem,3.2vw,2.7rem);margin:1rem 0 1.5rem;color:var(--navy)">A company delivering strategic business solutions.</h2>
          <p><strong>KNC Logistics Solutions</strong> is a Foreign Investment Company (LLC), established in 2026 and headquartered in Riyadh, Kingdom of Saudi Arabia.</p>
          <p>Since our inception, we have been committed to delivering innovative, reliable, and value-driven business solutions that empower organizations to achieve operational excellence and sustainable growth.</p>
          <p>With a diversified portfolio of services, KNC Logistics Solutions operates across multiple strategic sectors, including International Freight Forwarding, Customs Clearance, Inland Transportation, Warehousing & Distribution, Ship Supply, Software Development, Business Consultancy, Oilfield Stores & Industrial Supplies, and other integrated commercial services.</p>
          <p>By bringing these capabilities under one roof, we provide our clients with seamless end-to-end solutions that simplify operations and enhance business performance.</p>
          <p>As Saudi Arabia continues its remarkable transformation under Vision 2030, we are proud to contribute to the Kingdom's economic diversification by providing world-class logistics, technology, and business solutions that connect businesses with opportunities locally and globally.</p>
        </div>
      </div>
'''
    html = re.sub(r'<div class="who-grid">.*?<!-- LEADERSHIP TEAM -->', who_we_are_html + '\n      <!-- LEADERSHIP TEAM -->', html, flags=re.IGNORECASE | re.DOTALL)
    
    # 5. Professional Team (replacing Leadership Team)
    prof_team_html = '''
      <!-- PROFESSIONAL TEAM -->
      <div class="leadership-area">
        <div class="section-head centered reveal">
          <span class="eyebrow">Professional Team</span>
          <h2>Experienced professionals</h2>
          <p>At KNC Logistics Service, our strength lies in our people. We are proud to have a diverse and highly skilled team of professionals who bring together deep industry knowledge, technical expertise, and a shared commitment to excellence. Our team is the driving force behind our success and the foundation of the trusted relationships we build with our clients.</p>
        </div>

        <div class="values-grid" style="margin-top: 3rem;">
          <div class="value-card reveal" style="padding: 2rem 1.5rem;">
            <h3 style="font-size: 1.1rem; text-align: center;">Experienced Logistics Professionals</h3>
          </div>
          <div class="value-card reveal" style="padding: 2rem 1.5rem;">
            <h3 style="font-size: 1.1rem; text-align: center;">End-to-End Supply Chain Expertise</h3>
          </div>
          <div class="value-card reveal" style="padding: 2rem 1.5rem;">
            <h3 style="font-size: 1.1rem; text-align: center;">Project Logistics Capability</h3>
          </div>
          <div class="value-card reveal" style="padding: 2rem 1.5rem;">
            <h3 style="font-size: 1.1rem; text-align: center;">Freight Forwarding Expertise</h3>
          </div>
          <div class="value-card reveal" style="padding: 2rem 1.5rem;">
            <h3 style="font-size: 1.1rem; text-align: center;">Technology-Driven Operations</h3>
          </div>
          <div class="value-card reveal" style="padding: 2rem 1.5rem;">
            <h3 style="font-size: 1.1rem; text-align: center;">Strong Vendor &amp; Subcontractor Network</h3>
          </div>
        </div>
      </div>
'''
    html = re.sub(r'<!-- LEADERSHIP TEAM -->.*?</div>\s*</div>\s*</section>', prof_team_html + '\n    </div>\n  </section>', html, flags=re.IGNORECASE | re.DOTALL)

    # 6. Vision & Mission
    vision_mission_html = '''
  <!-- VISION & MISSION — IMMERSIVE FULL-WIDTH -->
  <section class="vm-section" id="vision">
    <div class="section-head centered reveal" style="padding:5rem 5vw 0">
      <span class="eyebrow">Company Vision &amp; Mission</span>
      <h2>Building lasting value, deliberately.</h2>
    </div>

    <!-- VISION CARD -->
    <div class="vm-card-full reveal-left">
      <div class="vm-card-bg">
        <img src="images/vision.png" alt="Global vision — city skyline at golden hour" loading="lazy">
      </div>
      <div class="vm-card-overlay"></div>
      <div class="vm-card-content" style="max-width: 800px;">
        <span class="eyebrow">Our Vision</span>
        <p style="font-size: 1.3rem; line-height: 1.8; color: #fff; margin-top: 1rem;">To become a globally recognized diversified holding group, delivering integrated and innovative solutions across logistics, healthcare, industrial services, trade, and business advisory &mdash; creating lasting value for stakeholders and contributing to sustainable economic progress across the markets we serve</p>
      </div>
      <div class="vm-card-decorline"></div>
    </div>

    <!-- MISSION CARD -->
    <div class="vm-card-full reveal-right">
      <div class="vm-card-bg">
        <img src="images/mission.png" alt="Mission — collaborative workspace from above" loading="lazy">
      </div>
      <div class="vm-card-overlay"></div>
      <div class="vm-card-content" style="max-width: 800px;">
        <span class="eyebrow">Our Mission</span>
        <p style="font-size: 1.3rem; line-height: 1.8; color: #fff; margin-top: 1rem;">To deliver integrated, innovative, and value-driven solutions across our diverse portfolio of businesses by fostering excellence, embracing technology, developing exceptional talent, and building strategic partnerships &mdash; empowering our clients and creating sustainable value for our stakeholders.</p>
      </div>
      <div class="vm-card-decorline"></div>
    </div>
  </section>
'''
    html = re.sub(r'<!-- VISION & MISSION — IMMERSIVE FULL-WIDTH -->.*?<!-- CORE VALUES — 4 CARDS -->', vision_mission_html + '\n  <!-- CORE VALUES — 4 CARDS -->', html, flags=re.IGNORECASE | re.DOTALL)

    # Remove Core values section as it's not supported by PDF
    html = re.sub(r'<!-- CORE VALUES — 4 CARDS -->.*?<div class="section-divider"></div>', '<div class="section-divider"></div>', html, flags=re.IGNORECASE | re.DOTALL)

    # 7. Our Services
    services_html = '''
  <!-- SERVICES -->
  <section class="alt" id="services">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">What we offer</span>
        <h2>Our Services</h2>
      </div>
      <div class="services-grid" style="grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));">
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">01</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">Freight Forwarding</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">02</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">Customs Clearance</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">03</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">In Land &amp; Cross border Transport</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">04</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">Project Logistics</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">05</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">Event Logistics</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">06</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">Rental Services</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">07</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">4PL Services</h3>
        </div>
        <div class="service-card reveal" style="padding: 2rem;">
          <div class="service-index">08</div>
          <h3 style="margin-top: 1rem; font-size: 1.25rem;">SABER Services</h3>
        </div>
      </div>
    </div>
  </section>
'''
    html = re.sub(r'<!-- SERVICES -->.*?<!-- WHY CHOOSE US -->', services_html + '\n  <!-- WHY CHOOSE US -->', html, flags=re.IGNORECASE | re.DOTALL)

    # 8. Why KNC
    why_html = '''
  <!-- WHY KNC -->
  <section id="why">
    <div class="wrap">
      <div class="section-head reveal">
        <span class="eyebrow">Why KNC</span>
        <h2>Building long-term relationships</h2>
        <p>We establish strong and lasting relationships with clients and partners through transparency and professionalism.</p>
      </div>
      <div class="why-grid">
        <div class="why-card reveal">
          <div class="why-num">01</div>
          <h3>One Partner. Complete Logistics.</h3>
        </div>
        <div class="why-card reveal">
          <div class="why-num">02</div>
          <h3>We Own the Execution</h3>
        </div>
        <div class="why-card reveal">
          <div class="why-num">03</div>
          <h3>Right Resources, Right Time</h3>
        </div>
        <div class="why-card reveal">
          <div class="why-num">04</div>
          <h3>Local Knowledge. Global Standards.</h3>
        </div>
        <div class="why-card reveal">
          <div class="why-num">05</div>
          <h3>Visibility at Every Stage</h3>
        </div>
        <div class="why-card reveal">
          <div class="why-num">06</div>
          <h3>Safety Is Non-Negotiable.</h3>
        </div>
      </div>
    </div>
  </section>
'''
    html = re.sub(r'<!-- WHY CHOOSE US -->.*?<!-- CONTACT -->', why_html + '\n  <!-- CONTACT -->', html, flags=re.IGNORECASE | re.DOTALL)

    # 9. Contact Section
    contact_html = '''
  <!-- CONTACT -->
  <section class="contact-section" id="contact">
    <div class="wrap">
      <div class="contact-inner">
        <div class="reveal-left" style="width: 100%;">
          <span class="eyebrow">CONTACT US</span>
          <h2 class="contact-left-h">Let's build success<br><em style="font-style:italic;color:var(--copper-lt)">together</em></h2>
          <div class="contact-cards" style="margin-top: 3rem;">
            <div class="contact-card">
              <div class="contact-card-icon">&#128222;</div>
              <div>
                <div class="contact-card-label">Phone</div>
                <div class="contact-card-value">0502746895</div>
              </div>
            </div>
            <div class="contact-card">
              <div class="contact-card-icon">&#9993;</div>
              <div>
                <div class="contact-card-label">Email</div>
                <div class="contact-card-value">info@masteryandprecise.com</div>
              </div>
            </div>
            <div class="contact-card">
              <div class="contact-card-icon">&#127760;</div>
              <div>
                <div class="contact-card-label">Website</div>
                <div class="contact-card-value">www.masteryandprecise.com</div>
              </div>
            </div>
            <div class="contact-card">
              <div class="contact-card-icon">&#128205;</div>
              <div>
                <div class="contact-card-label">Location</div>
                <div class="contact-card-value">RIYADH - SAUDI ARABIA</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''
    html = re.sub(r'<!-- CONTACT -->.*?<!-- FOOTER -->', contact_html + '\n  <!-- FOOTER -->', html, flags=re.IGNORECASE | re.DOTALL)

    # Footer
    html = re.sub(r'<span\s*style="font-family: \'Fraunces\', serif; font-weight: 700; font-size: 1.6rem; color: #fff; letter-spacing: 0.03em; white-space: nowrap;">MASTERY\s*&amp; PRECISE</span>', '<span\n                style="font-family: \'Fraunces\', serif; font-weight: 700; font-size: 1.6rem; color: #fff; letter-spacing: 0.03em; white-space: nowrap;">KNC LOGISTICS SERVICES</span>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<span\s*style="font-family: \'Space Grotesk\', sans-serif; font-size: 0.6rem; letter-spacing: 0.18em; text-transform: uppercase; color: #c9870a; font-weight: 600;">Business\s*House Private Limited</span>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<span\s*style="font-family: \'Space Grotesk\', sans-serif; font-size: 0.5rem; letter-spacing: 0.2em; text-transform: uppercase; color: rgba\(255,255,255,0.45\); white-space: nowrap; margin-top: 4px;">Mastery\s*in Vision. Precise in Action.</span>', '<span\n                style="font-family: \'Space Grotesk\', sans-serif; font-size: 0.6rem; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(255,255,255,0.45); white-space: nowrap; margin-top: 4px;">Strategic Business Solutions</span>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<p>A multidisciplinary consulting organization helping businesses achieve sustainable growth through strategic\s*advisory, operational excellence, and digital transformation.</p>', '<p>A company delivering strategic business solutions. Committed to delivering innovative, reliable, and value-driven business solutions.</p>', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<li><a href="knc-logistics\.html">KNC Logistics</a></li>', '', html, flags=re.IGNORECASE | re.DOTALL)
    
    # footer services
    footer_services_html = '''
          <ul>
            <li><a href="#services">Freight Forwarding</a></li>
            <li><a href="#services">Customs Clearance</a></li>
            <li><a href="#services">In Land &amp; Cross border Transport</a></li>
            <li><a href="#services">Project Logistics</a></li>
            <li><a href="#services">Event Logistics</a></li>
          </ul>
'''
    html = re.sub(r'<h4>Services</h4>\s*<ul>.*?</ul>', '<h4>Services</h4>' + footer_services_html, html, flags=re.IGNORECASE | re.DOTALL)

    # footer tagline & copy
    html = re.sub(r'<p class="footer-tagline">Mastery in Vision\. Precise in Action\.</p>', '', html, flags=re.IGNORECASE | re.DOTALL)
    html = re.sub(r'<mark>Mastery &amp; Precise Business House Private Limited</mark>', '<mark>KNC Logistics Services</mark>', html, flags=re.IGNORECASE | re.DOTALL)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        
update_html()
