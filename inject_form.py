import re

with open('c:/Elevix Digital/contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section = """
    <!-- Combined Form & Direct Line Section -->
    <section class="relative bg-deep-obsidian py-32 overflow-hidden z-10 border-t border-white/5">
        <div class="max-w-7xl mx-auto px-6 md:px-12 lg:px-16 grid grid-cols-1 lg:grid-cols-12 gap-16 lg:gap-24">
            
            <!-- Left Column: The Form (Col span 7) -->
            <div class="lg:col-span-7">
                <!-- Header -->
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-[1px] bg-kinetic-red"></div>
                    <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 01. START A PROJECT</span>
                </div>
                
                <h2 class="font-display font-bold text-[40px] md:text-[55px] text-white leading-[1.05] tracking-tight mb-6">
                    Tell us the shape of the<br/>problem.
                </h2>
                
                <p class="font-display text-[16px] text-[#999] leading-[1.7] max-w-xl mb-12 font-medium">
                    Six fields, under two minutes. Share the revenue goal you're chasing and what's blocking it &mdash; we'll come back with either a strategy call or a clear referral.
                </p>
                
                <!-- Form Box -->
                <div class="bg-[#0e0e0e] border border-white/5 rounded-2xl p-8 md:p-10 shadow-[0_0_50px_rgba(0,0,0,0.5)]">
                    <!-- Form Inner Header -->
                    <div class="flex justify-between items-center mb-10 pb-6 border-b border-white/5">
                        <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// START A PROJECT</span>
                        <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">~4 HR RESPONSE</span>
                    </div>
                    
                    <!-- Form Fields -->
                    <form class="space-y-8">
                        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                            <!-- Full Name -->
                            <div>
                                <label class="block font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase mb-3">FULL NAME</label>
                                <input type="text" placeholder="e.g. Ahmed Ali" class="w-full bg-[#141414] border border-white/5 rounded-md px-5 py-4 text-[14px] text-white font-medium placeholder-[#555] focus:outline-none focus:border-kinetic-red focus:ring-1 focus:ring-kinetic-red transition-all">
                            </div>
                            <!-- Email -->
                            <div>
                                <label class="block font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase mb-3">EMAIL</label>
                                <input type="email" placeholder="you@company.com" class="w-full bg-[#141414] border border-white/5 rounded-md px-5 py-4 text-[14px] text-white font-medium placeholder-[#555] focus:outline-none focus:border-kinetic-red focus:ring-1 focus:ring-kinetic-red transition-all">
                            </div>
                            <!-- Phone -->
                            <div>
                                <label class="block font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase mb-3">PHONE</label>
                                <input type="tel" placeholder="+92 300 0000000" class="w-full bg-[#141414] border border-white/5 rounded-md px-5 py-4 text-[14px] text-white font-medium placeholder-[#555] focus:outline-none focus:border-kinetic-red focus:ring-1 focus:ring-kinetic-red transition-all">
                            </div>
                            <!-- Company -->
                            <div>
                                <label class="block font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase mb-3">COMPANY</label>
                                <input type="text" placeholder="Your brand or business" class="w-full bg-[#141414] border border-white/5 rounded-md px-5 py-4 text-[14px] text-white font-medium placeholder-[#555] focus:outline-none focus:border-kinetic-red focus:ring-1 focus:ring-kinetic-red transition-all">
                            </div>
                        </div>
                        
                        <!-- Service Interested In -->
                        <div>
                            <label class="block font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase mb-3">SERVICE INTERESTED IN</label>
                            <select class="w-full bg-[#141414] border border-white/5 rounded-md px-5 py-4 text-[14px] text-white font-medium focus:outline-none focus:border-kinetic-red focus:ring-1 focus:ring-kinetic-red transition-all appearance-none">
                                <option>AI Automation</option>
                                <option>Web Development</option>
                                <option>Digital Marketing</option>
                                <option>App Development</option>
                                <option>SEO Services</option>
                            </select>
                        </div>
                        
                        <!-- Textarea -->
                        <div>
                            <label class="block font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase mb-3">WHAT ARE YOU TRYING TO SCALE? (OPTIONAL)</label>
                            <textarea rows="4" placeholder="Revenue goal, what you have tried, what blocking you right now." class="w-full bg-[#141414] border border-white/5 rounded-md px-5 py-4 text-[14px] text-white font-medium placeholder-[#555] focus:outline-none focus:border-kinetic-red focus:ring-1 focus:ring-kinetic-red transition-all resize-none"></textarea>
                        </div>
                        
                        <!-- Submit Area -->
                        <div class="flex flex-col md:flex-row justify-between items-center gap-6 pt-6 border-t border-white/5">
                            <span class="font-mono text-[10px] text-[#666] tracking-[0.1em] font-bold uppercase text-center md:text-left leading-relaxed">
                                WE NEVER SPAM. YOUR DETAILS REACH THE FOUNDER DIRECTLY.
                            </span>
                            <button type="submit" class="bg-kinetic-red text-white px-8 py-4 rounded-md font-display font-bold text-[14px] hover:bg-[#d42023] transition-colors shadow-[0_0_20px_rgba(232,40,43,0.3)] flex items-center gap-2 group whitespace-nowrap">
                                Send it 
                                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" class="group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                            </button>
                        </div>
                    </form>
                </div>
                
                <!-- Privacy Disclaimer -->
                <p class="font-mono text-[9px] text-[#555] tracking-[0.1em] font-bold uppercase mt-8 leading-relaxed max-w-xl">
                    BY SUBMITTING, YOU AGREE TO OUR <a href="#" class="text-white hover:text-kinetic-red transition-colors underline decoration-white/20 underline-offset-4">PRIVACY POLICY</a>. WE NEVER SHARE YOUR DETAILS WITH THIRD PARTIES.
                </p>
            </div>
            
            
            <!-- Right Column: Direct Line (Col span 5) -->
            <div class="lg:col-span-5">
                <!-- Header -->
                <div class="flex items-center gap-4 mb-6">
                    <div class="w-12 h-[1px] bg-kinetic-red"></div>
                    <span class="font-mono text-[10px] text-kinetic-red tracking-[0.2em] font-bold uppercase">// 02. DIRECT LINE</span>
                </div>
                
                <h3 class="font-display font-bold text-[30px] md:text-[35px] text-white leading-[1.1] tracking-tight mb-4">
                    Prefer not to fill a form?
                </h3>
                
                <p class="font-display text-[15px] text-[#999] leading-[1.6] mb-10 font-medium">
                    Pick the channel that suits you. All three reach a human on the Elevix team &mdash; not a ticketing queue.
                </p>
                
                <div class="space-y-4">
                    <!-- WhatsApp Card -->
                    <div class="bg-[#0e0e0e] border border-white/5 rounded-xl p-6 hover:border-white/20 transition-all cursor-pointer group relative">
                        <div class="flex justify-between items-start mb-6">
                            <div class="flex items-center gap-3">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="2"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
                                <span class="font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase">WHATSAPP</span>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" class="group-hover:stroke-white transition-colors"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                        </div>
                        <h4 class="font-display font-bold text-[22px] text-white mb-2 tracking-tight">+92 300 000</h4>
                        <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">FASTEST - REPLIES WITHIN THE HOUR</span>
                    </div>
                    
                    <!-- Call Card -->
                    <div class="bg-[#0e0e0e] border border-white/5 rounded-xl p-6 hover:border-white/20 transition-all cursor-pointer group relative">
                        <div class="flex justify-between items-start mb-6">
                            <div class="flex items-center gap-3">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
                                <span class="font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase">CALL</span>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" class="group-hover:stroke-white transition-colors"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                        </div>
                        <h4 class="font-display font-bold text-[22px] text-white mb-2 tracking-tight">+92 300 000</h4>
                        <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">MON-SAT &bull; 09:30-18:00 PKT</span>
                    </div>
                    
                    <!-- Email Card -->
                    <div class="bg-[#0e0e0e] border border-white/5 rounded-xl p-6 hover:border-white/20 transition-all cursor-pointer group relative">
                        <div class="flex justify-between items-start mb-6">
                            <div class="flex items-center gap-3">
                                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#E8282B" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"></rect><path d="M2 4l10 8 10-8"></path></svg>
                                <span class="font-mono text-[10px] text-[#666] tracking-[0.2em] font-bold uppercase">EMAIL</span>
                            </div>
                            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2" class="group-hover:stroke-white transition-colors"><path d="M7 17l9.2-9.2M17 17V7H7"/></svg>
                        </div>
                        <h4 class="font-display font-bold text-[22px] text-white mb-2 tracking-tight">info@elevix.com</h4>
                        <span class="font-mono text-[10px] text-[#555] tracking-[0.2em] font-bold uppercase">FOUNDER-READ &bull; ~4 HR REPLY</span>
                    </div>
                    
                    <!-- Testimonial -->
                    <div class="bg-[#0e0e0e] border border-white/5 rounded-xl p-8 mt-8">
                        <div class="flex justify-between items-start mb-6">
                            <div class="flex items-center gap-4">
                                <div class="w-12 h-12 rounded-full bg-[#1a1a1a] border border-white/10 overflow-hidden flex items-center justify-center">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#666" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
                                </div>
                                <div>
                                    <h5 class="font-display font-bold text-white text-[15px]">Safwan Rasheed</h5>
                                    <span class="font-mono text-[9px] text-[#666] tracking-[0.1em] font-bold uppercase">HEAD OF OPERATIONS &bull; PAKISTAN</span>
                                </div>
                            </div>
                            <!-- 5 Stars -->
                            <div class="flex gap-1">
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="#fbbf24" stroke="#fbbf24" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="#fbbf24" stroke="#fbbf24" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="#fbbf24" stroke="#fbbf24" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="#fbbf24" stroke="#fbbf24" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                                <svg width="12" height="12" viewBox="0 0 24 24" fill="#fbbf24" stroke="#fbbf24" stroke-width="2"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
                            </div>
                        </div>
                        <p class="font-display text-[14px] text-[#ccc] leading-[1.6] font-medium mb-6">
                            "We got Elevix on board and they've easily been the best AI automation agency in Pakistan for us. They set up our complete digital sales system and we've been hitting an incredible ROI. The Return On Investment was way beyond what we expected. If you want an agency that actually gets you results, just go with Elevix. Highly recommended!"
                        </p>
                        <div class="inline-block border border-kinetic-red/30 rounded-full px-3 py-1">
                            <span class="font-mono text-[9px] text-kinetic-red tracking-[0.2em] font-bold uppercase">20X ROAS</span>
                        </div>
                    </div>

                </div>
            </div>
            
        </div>
    </section>
"""

# Insert right before the footer
footer_index = content.find("<!-- Footer -->")
if footer_index != -1:
    final_content = content[:footer_index] + new_section + "\n" + content[footer_index:]
    with open('c:/Elevix Digital/contact.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Successfully injected the combined section into contact.html!")
else:
    print("Error: Could not find <!-- Footer -->")
