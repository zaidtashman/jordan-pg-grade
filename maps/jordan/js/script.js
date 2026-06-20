document.addEventListener('DOMContentLoaded', () => {
    
    // --- Elements ---
    const langEnBtn = document.getElementById('lang-en');
    const langArBtn = document.getElementById('lang-ar');
    const htmlTag = document.documentElement;
    
    const sidebar = document.getElementById('sidebar');
    const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
    const closeSidebarBtn = document.getElementById('close-sidebar');
    const sidebarBackdrop = document.getElementById('sidebar-backdrop');

    // --- Language Management ---
    
    // Function to set language
    const setLanguage = (lang) => {
        // Update HTML attributes
        htmlTag.lang = lang;
        htmlTag.dir = lang === 'ar' ? 'rtl' : 'ltr';
        
        // Update Buttons
        if (lang === 'ar') {
            langArBtn.classList.add('active');
            langEnBtn.classList.remove('active');
        } else {
            langEnBtn.classList.add('active');
            langArBtn.classList.remove('active');
        }

        // Update all elements with data-en and data-ar attributes
        const translatableElements = document.querySelectorAll('[data-en][data-ar]');
        translatableElements.forEach(el => {
            el.textContent = el.getAttribute(`data-${lang}`);
        });
        
        // Save preference
        localStorage.setItem('preferredLang', lang);
    };

    // Initialize Language
    const savedLang = localStorage.getItem('preferredLang') || 'en';
    setLanguage(savedLang);

    // Event Listeners for Language Toggle
    langEnBtn.addEventListener('click', () => setLanguage('en'));
    langArBtn.addEventListener('click', () => setLanguage('ar'));


    // --- Mobile Sidebar Management ---
    
    const openSidebar = () => {
        sidebar.classList.add('active');
        sidebarBackdrop.classList.add('active');
    };
    
    const closeSidebar = () => {
        sidebar.classList.remove('active');
        sidebarBackdrop.classList.remove('active');
    };

    if (mobileMenuToggle) {
        mobileMenuToggle.addEventListener('click', openSidebar);
    }
    
    if (closeSidebarBtn) {
        closeSidebarBtn.addEventListener('click', closeSidebar);
    }
    
    if (sidebarBackdrop) {
        sidebarBackdrop.addEventListener('click', closeSidebar);
    }
    
    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && sidebar.classList.contains('active')) {
            closeSidebar();
        }
    });

});
