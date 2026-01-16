# 🚀 AnalizDestek Ana Sayfa Widget'ları - Entegrasyon Rehberi

## 📦 Paket İçeriği

1. **AnalizDestek_Homepage_Widgets.html** - Widget tasarımları ve örnek HTML
2. Bu doküman - Implementasyon rehberi

---

## 🎯 WİDGET 1: Gerçek Zamanlı İstatistikler

### Görsel:
```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ 🟢 Şu Anda      │ Bu Hafta        │ Son 24 Saatte   │ Toplam Uzman    │
│    Online       │ Çözülen         │                 │                 │
│      23         │      87         │      156        │      342        │
│ Aktif Kullanıcı │    Soru         │  Yeni Gönderi   │   Aktif Üye     │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

### Backend Gereksinimleri:
```javascript
// API Endpoint'leri (önerilen)
GET /api/stats/online-users     // Şu anda online kaç kişi
GET /api/stats/solved-weekly    // Bu hafta çözülen soru sayısı
GET /api/stats/posts-24h        // Son 24 saatteki gönderi sayısı
GET /api/stats/total-experts    // Toplam aktif uzman sayısı
```

### Örnek JSON Response:
```json
{
  "onlineUsers": 23,
  "solvedWeekly": 87,
  "posts24h": 156,
  "totalExperts": 342,
  "timestamp": "2026-01-16T10:30:00Z"
}
```

### Frontend Kodu (React örneği):
```jsx
import { useState, useEffect } from 'react';

function StatsWidget() {
  const [stats, setStats] = useState({
    onlineUsers: 0,
    solvedWeekly: 0,
    posts24h: 0,
    totalExperts: 0
  });

  useEffect(() => {
    // İlk yükleme
    fetchStats();
    
    // Her 10 saniyede bir güncelle
    const interval = setInterval(fetchStats, 10000);
    return () => clearInterval(interval);
  }, []);

  const fetchStats = async () => {
    const response = await fetch('/api/stats');
    const data = await response.json();
    setStats(data);
  };

  return (
    <div className="stats-grid">
      <div className="stat-card green">
        <div className="stat-label">
          <span className="online-indicator"></span>Şu Anda Online
        </div>
        <div className="stat-number">{stats.onlineUsers}</div>
        <div className="stat-label">Aktif Kullanıcı</div>
      </div>
      {/* Diğer kartlar... */}
    </div>
  );
}
```

### Database Query Örnekleri (PostgreSQL):
```sql
-- Online kullanıcılar (son 5 dakikada aktivite gösterenler)
SELECT COUNT(DISTINCT user_id) 
FROM user_sessions 
WHERE last_activity > NOW() - INTERVAL '5 minutes';

-- Bu hafta çözülen sorular
SELECT COUNT(*) 
FROM questions 
WHERE status = 'solved' 
  AND solved_at >= DATE_TRUNC('week', NOW());

-- Son 24 saatte yeni gönderiler
SELECT COUNT(*) 
FROM posts 
WHERE created_at >= NOW() - INTERVAL '24 hours';

-- Toplam aktif uzmanlar (son 30 günde yanıt verenler)
SELECT COUNT(DISTINCT user_id) 
FROM answers 
WHERE created_at >= NOW() - INTERVAL '30 days'
  AND user_reputation >= 100;
```

---

## 💬 WİDGET 2: Son Tartışmalar

### Görsel:
```
┌──────────────────────────────────────────────────────────┐
│ [SS] SPSS'te normallik testi sonuçlarını nasıl...  [YENİ]│
│      👤 YeniAraştırmacı23 💬 12 yanıt 🕐 2 dk önce ✅     │
├──────────────────────────────────────────────────────────┤
│ [PY] Python pandas ile Excel dosyası nasıl okunur?      │
│      👤 PythonYolcusu 💬 8 yanıt 🕐 15 dk önce           │
└──────────────────────────────────────────────────────────┘
```

### Backend API:
```javascript
GET /api/discussions/recent?limit=5

// Response:
{
  "discussions": [
    {
      "id": 1234,
      "title": "SPSS'te normallik testi sonuçlarını nasıl yorumlarım?",
      "author": {
        "id": 567,
        "username": "YeniAraştırmacı23",
        "avatar": "https://..."
      },
      "category": "SPSS",
      "replyCount": 12,
      "viewCount": 234,
      "createdAt": "2026-01-16T10:28:00Z",
      "isSolved": true,
      "isNew": true,  // Son 1 saat içinde oluşturulmuş
      "isHot": false  // 50+ yanıt veya 500+ görüntülenme
    },
    // ...
  ]
}
```

### Frontend Kodu:
```jsx
function RecentDiscussions() {
  const [discussions, setDiscussions] = useState([]);

  useEffect(() => {
    fetch('/api/discussions/recent?limit=5')
      .then(res => res.json())
      .then(data => setDiscussions(data.discussions));
  }, []);

  const getTimeAgo = (timestamp) => {
    // "2 dakika önce", "1 saat önce" formatına çevir
    const diff = Date.now() - new Date(timestamp);
    const minutes = Math.floor(diff / 60000);
    if (minutes < 60) return `${minutes} dakika önce`;
    const hours = Math.floor(minutes / 60);
    return `${hours} saat önce`;
  };

  return (
    <ul className="recent-discussions">
      {discussions.map(d => (
        <li key={d.id} className="discussion-item">
          <div className="discussion-icon">
            {d.category.substring(0, 2).toUpperCase()}
          </div>
          <div className="discussion-content">
            <div className="discussion-title">
              {d.title}
              {d.isNew && <span className="discussion-badge new">YENİ</span>}
              {d.isHot && <span className="discussion-badge">HOT 🔥</span>}
            </div>
            <div className="discussion-meta">
              <span>👤 {d.author.username}</span>
              <span>💬 {d.replyCount} yanıt</span>
              <span>🕐 {getTimeAgo(d.createdAt)}</span>
              {d.isSolved && <span>✅ Çözüldü</span>}
            </div>
          </div>
        </li>
      ))}
    </ul>
  );
}
```

### Database Query:
```sql
SELECT 
  q.id,
  q.title,
  q.created_at,
  q.is_solved,
  u.id as author_id,
  u.username as author_username,
  c.name as category,
  COUNT(DISTINCT a.id) as reply_count,
  q.view_count,
  CASE WHEN q.created_at >= NOW() - INTERVAL '1 hour' THEN true ELSE false END as is_new,
  CASE WHEN COUNT(DISTINCT a.id) >= 50 OR q.view_count >= 500 THEN true ELSE false END as is_hot
FROM questions q
LEFT JOIN users u ON q.author_id = u.id
LEFT JOIN categories c ON q.category_id = c.id
LEFT JOIN answers a ON q.id = a.question_id
GROUP BY q.id, u.id, c.name
ORDER BY q.created_at DESC
LIMIT 5;
```

---

## 🔥 WİDGET 3: Bu Hafta Popüler

### Backend API:
```javascript
GET /api/discussions/popular?period=week&limit=4

// Response:
{
  "topics": [
    {
      "id": 789,
      "title": "Cronbach Alpha 0.68 kabul edilir mi?",
      "viewCount": 412,
      "replyCount": 25,
      "category": "Güvenilirlik"
    },
    // ...
  ]
}
```

### Database Query:
```sql
-- Popülerlik skoru: (görüntülenme * 0.3) + (yanıt * 2)
SELECT 
  id,
  title,
  view_count,
  reply_count,
  (view_count * 0.3 + reply_count * 2) as popularity_score
FROM (
  SELECT 
    q.id,
    q.title,
    q.view_count,
    COUNT(DISTINCT a.id) as reply_count
  FROM questions q
  LEFT JOIN answers a ON q.id = a.question_id
  WHERE q.created_at >= DATE_TRUNC('week', NOW())
  GROUP BY q.id
) subquery
ORDER BY popularity_score DESC
LIMIT 4;
```

---

## ⚡ WİDGET 4: Canlı Aktivite Feed

### Backend: WebSocket veya Server-Sent Events (SSE)

**WebSocket Yaklaşımı:**
```javascript
// Backend (Node.js + Socket.io)
io.on('connection', (socket) => {
  console.log('User connected');
  
  // Yeni aktivite olduğunda yayınla
  socket.on('new_activity', (data) => {
    io.emit('activity_update', {
      user: data.username,
      action: data.action,
      timestamp: new Date()
    });
  });
});

// Frontend
import io from 'socket.io-client';

function ActivityFeed() {
  const [activities, setActivities] = useState([]);
  
  useEffect(() => {
    const socket = io('https://analizdestek-ai.onrender.com');
    
    socket.on('activity_update', (activity) => {
      setActivities(prev => [activity, ...prev].slice(0, 10));
    });
    
    return () => socket.disconnect();
  }, []);
  
  return (
    <div className="activity-feed">
      {activities.map((a, i) => (
        <div key={i} className="activity-item">
          <div className="activity-avatar">
            {a.user.substring(0, 2).toUpperCase()}
          </div>
          <div className="activity-text">
            <span className="username">{a.user}</span> {a.action}
          </div>
          <div className="activity-time">{getTimeAgo(a.timestamp)}</div>
        </div>
      ))}
    </div>
  );
}
```

**Alternatif: Polling (Daha Basit)**
```javascript
// Her 10 saniyede API çağır
useEffect(() => {
  const fetchActivities = async () => {
    const res = await fetch('/api/activities/recent?limit=10');
    const data = await res.json();
    setActivities(data.activities);
  };
  
  fetchActivities();
  const interval = setInterval(fetchActivities, 10000);
  return () => clearInterval(interval);
}, []);
```

### Database Query:
```sql
-- Son aktiviteleri getir (union ile birleştir)
(
  SELECT 
    'answer' as type,
    u.username,
    'bir yanıt verdi' as action,
    a.created_at as timestamp
  FROM answers a
  JOIN users u ON a.user_id = u.id
  ORDER BY a.created_at DESC
  LIMIT 5
)
UNION ALL
(
  SELECT 
    'question' as type,
    u.username,
    'yeni bir soru açtı' as action,
    q.created_at as timestamp
  FROM questions q
  JOIN users u ON q.user_id = u.id
  ORDER BY q.created_at DESC
  LIMIT 5
)
ORDER BY timestamp DESC
LIMIT 10;
```

---

## 🎨 CSS Dosyası (Entegrasyon için)

Mevcut sitenize ekleyeceğiniz CSS:

```css
/* Ana Sayfa Widget'ları */
.homepage-widgets {
  max-width: 1200px;
  margin: 40px auto;
  padding: 0 20px;
}

/* Stats Grid */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
  margin-bottom: 40px;
}

.stat-card {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px;
  border-radius: 10px;
  text-align: center;
  transition: transform 0.3s;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-number {
  font-size: 2.5em;
  font-weight: bold;
  margin: 10px 0;
}

.online-indicator {
  display: inline-block;
  width: 10px;
  height: 10px;
  background: #2ecc71;
  border-radius: 50%;
  margin-right: 5px;
  animation: blink 1.5s infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.3; }
}

/* Son Tartışmalar */
.recent-discussions {
  list-style: none;
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

.discussion-item {
  display: flex;
  padding: 15px;
  border-bottom: 1px solid #ecf0f1;
  transition: background 0.3s;
}

.discussion-item:hover {
  background: #f8f9fa;
  cursor: pointer;
}

.discussion-badge.new {
  background: #e74c3c;
  animation: pulse 2s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.6; }
}
```

---

## 📱 Responsive Tasarım

Widget'lar mobilde şu şekilde davranmalı:

```css
@media (max-width: 768px) {
  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  
  .stat-card {
    padding: 15px;
  }
  
  .stat-number {
    font-size: 2em;
  }
  
  .discussion-item {
    flex-direction: column;
  }
  
  .discussion-icon {
    margin-bottom: 10px;
  }
}
```

---

## 🔧 Uygulama Adımları (Önerilen Sıra)

### Aşama 1: Mock Data ile Test (1 gün)
1. HTML dosyasını indir ve tarayıcıda aç
2. Tasarımı test et, gerekirse renkleri ayarla
3. Mock (sahte) verilerle frontend'i tamamla

### Aşama 2: Backend API'ler (2-3 gün)
1. `/api/stats` endpoint'ini oluştur
2. `/api/discussions/recent` endpoint'ini oluştur
3. Database query'leri yaz ve test et
4. API response formatlarını doğrula

### Aşama 3: Frontend Entegrasyonu (1-2 gün)
1. React/Vue component'lerini oluştur
2. API'lere bağlan
3. Loading state'leri ekle
4. Error handling yap

### Aşama 4: Gerçek Zamanlı Özellikler (2 gün)
1. WebSocket veya polling seç
2. Canlı aktivite feed'i entegre et
3. Online kullanıcı sayacını aktif et

### Aşama 5: Optimizasyon (1 gün)
1. Caching ekle (Redis önerilir)
2. Rate limiting uygula
3. Performance test yap

---

## 💡 Bonus Öneriler

### 1. Caching Stratejisi
```javascript
// Redis ile cache (Node.js)
const redis = require('redis');
const client = redis.createClient();

async function getStats() {
  // Önce cache'e bak
  const cached = await client.get('stats:current');
  if (cached) return JSON.parse(cached);
  
  // Cache yoksa DB'den çek
  const stats = await db.query('SELECT ...');
  
  // 30 saniye cache'le
  await client.setex('stats:current', 30, JSON.stringify(stats));
  
  return stats;
}
```

### 2. Fake Data Generator (Geliştirme için)
```javascript
// Mock veri oluşturucu
function generateMockDiscussions(count) {
  const titles = [
    "SPSS'te normallik testi nasıl yapılır?",
    "Python pandas veri temizleme",
    "Regresyon analizi yorumlama",
    // ...
  ];
  
  return Array.from({ length: count }, (_, i) => ({
    id: i + 1,
    title: titles[Math.floor(Math.random() * titles.length)],
    author: { username: `User${i + 1}` },
    replyCount: Math.floor(Math.random() * 30),
    createdAt: new Date(Date.now() - Math.random() * 86400000)
  }));
}
```

### 3. Analytics Tracking
```javascript
// Widget etkileşimlerini takip et
function trackWidgetClick(widgetName, itemId) {
  fetch('/api/analytics/track', {
    method: 'POST',
    body: JSON.stringify({
      widget: widgetName,
      item: itemId,
      timestamp: new Date()
    })
  });
}
```

---

## 🚨 Dikkat Edilecekler

1. **Performance:**
   - İstatistikler için heavy query'ler cache'lenmel i
   - Canlı aktivite için WebSocket connection limit'i koy

2. **Security:**
   - API endpoint'lerine rate limiting ekle
   - SQL injection'a karşı prepared statements kullan

3. **UX:**
   - Loading skeleton'ları ekle
   - Error state'leri kullanıcı dostu yap
   - Animasyonları abartma (accessibility)

4. **SEO:**
   - Widget'lar SSR (Server-Side Rendering) ile render et
   - İlk yüklemede placeholder göster

---

## ✅ Başarı Kriterleri

Widget'lar şu kriterleri karşılamalı:
- [ ] Sayfa yüklenme süresi <2 saniye
- [ ] Online kullanıcı sayısı gerçek zamanlı güncelleniyor
- [ ] Son tartışmalar her 30 saniyede otomatik yenileniyor
- [ ] Mobilde düzgün görünüyor
- [ ] Accessibility standartlarına uygun (WCAG 2.1)
- [ ] Cross-browser uyumlu (Chrome, Firefox, Safari, Edge)

---

## 📞 Yardım & Destek

Entegrasyon sırasında sorun yaşarsan:
1. HTML örneğini tarayıcıda test et
2. Console'da JavaScript hatalarını kontrol et
3. Network tab'ında API response'ları incele

**Soru mu var?** Devam edelim! 🚀
