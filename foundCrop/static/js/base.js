// Naviguation Bar script

// $(document).ready(function() {
//     $("#sidebarCollapse").on("click", function() {
//       $("#sidebar").addClass("active");
//     });
  
//     $("#sidebarCollapseX").on("click", function() {
//       $("#sidebar").removeClass("active");
//     });
  
//     $("#sidebarCollapse").on("click", function() {
//       if ($("#sidebar").hasClass("active")) {
//         $(".overlay").addClass("visible");
//         console.log("it's working!");
//       }
//     });
  
//     $("#sidebarCollapseX").on("click", function() {
//       $(".overlay").removeClass("visible");
//     });
//   });

//   End of Navigation Bar script

/**
 * Hide and display side bar from Dashboard
 */
(function() {
    "use strict";
  
    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
      el = el.trim()
      if (all) {
        return [...document.querySelectorAll(el)]
      } else {
        return document.querySelector(el)
      }
    }
  
    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
      if (all) {
        select(el, all).forEach(e => e.addEventListener(type, listener))
      } else {
        select(el, all).addEventListener(type, listener)
      }
    }
  
    /**
     * Easy on scroll event listener
     */
    const onscroll = (el, listener) => {
      el.addEventListener('scroll', listener)
    }
  
    /**
     * Sidebar toggle
     */
    if (select('.toggle-sidebar-btn')) {
      on('click', '.toggle-sidebar-btn', function(e) {
        select('body').classList.toggle('toggle-sidebar')
      })
    }
  
    /**
     * Search bar toggle
     */
    if (select('.search-bar-toggle')) {
      on('click', '.search-bar-toggle', function(e) {
        select('.search-bar').classList.toggle('search-bar-show')
      })
    }
  })();
  
  /**
   * Display menu pop-up
   */
  $(function() {
    $('.popup').click(function() {
      $('.popuptext').toggle();
    });
  
  });