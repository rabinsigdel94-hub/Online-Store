# Promotional Banner Information

## 🎨 What Was Added

A beautiful rotating promotional banner/flyer at the top of the home page with 3 slides:

### Slide 1: MEGA SALE
- **Title**: "MEGA SALE - Up to 50% OFF!"
- **Badge**: 🔥 HOT DEALS
- **Features**: 
  - Nike, Adidas, Levi's & More
  - Free Shipping on Orders $50+
- **Button**: "Shop Now"

### Slide 2: NEW ARRIVALS
- **Title**: "Latest Fashion & Footwear"
- **Badge**: ✨ NEW ARRIVALS
- **Features**:
  - Trending Styles
  - Premium Brands
- **Button**: "Explore" (links to Clothing)

### Slide 3: SPECIAL OFFER
- **Title**: "Buy 2 Get 1 FREE!"
- **Badge**: 💎 EXCLUSIVE
- **Features**:
  - On Selected Items
  - Limited Time Only
- **Button**: "Shop Shoes" (links to Shoes category)

## 🎯 Features

- **Auto-rotating**: Changes every 5 seconds
- **Manual controls**: Left/right arrows to navigate
- **Indicators**: Dots at bottom to show current slide
- **Responsive**: Looks great on mobile and desktop
- **Animated**: Smooth transitions and pulse effect on badges
- **Gradient background**: Pink to red gradient
- **Icons**: FontAwesome icons for visual appeal

## 🎨 Design Elements

- **Colors**: Pink-to-red gradient (#f093fb to #f5576c)
- **Typography**: Bold white text with shadow
- **Buttons**: White buttons with hover effects
- **Animation**: Pulse effect on badges, smooth slide transitions
- **Shadow**: Elevated look with box shadow

## 📱 Responsive Design

- Desktop: Full layout with text and button side-by-side
- Mobile: Stacked layout, centered button
- All screen sizes: Maintains readability and appeal

## 🔧 How to Customize

### Change Banner Text
Edit `templates/products/home.html`:
- Find the carousel-item sections
- Update titles, badges, and text
- Modify button links and text

### Change Colors
Edit `templates/base.html` CSS:
```css
.promo-banner {
    background: linear-gradient(135deg, #YOUR_COLOR1, #YOUR_COLOR2);
}
```

### Change Auto-Rotate Speed
Add to carousel div:
```html
<div id="promoCarousel" class="carousel slide" data-bs-ride="carousel" data-bs-interval="3000">
```
(3000 = 3 seconds)

### Add More Slides
Copy a carousel-item div and:
1. Update the content
2. Add a new indicator button
3. Update data-bs-slide-to numbers

## 💡 Ideas for Future Banners

1. **Seasonal Sales**: "Summer Sale", "Black Friday", "Holiday Deals"
2. **Category Promotions**: "Electronics Week", "Fashion Friday"
3. **Brand Spotlights**: "Nike Day", "Adidas Special"
4. **Clearance**: "End of Season Clearance"
5. **New Launches**: "Just Arrived", "Coming Soon"

## 📊 Current Setup

- **Location**: Top of home page (above "Welcome to E-Store")
- **Auto-play**: Yes (5 seconds per slide)
- **Number of slides**: 3
- **Navigation**: Arrows + indicators
- **Mobile-friendly**: Yes

## 🚀 Next Steps

1. Refresh http://127.0.0.1:8000 to see the banner
2. Watch it auto-rotate through 3 promotional slides
3. Click arrows to manually navigate
4. Test on mobile view (resize browser)
5. Customize text and offers as needed

Your store now has a professional promotional banner that grabs attention! 🎉
