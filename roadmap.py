import os
import shutil

# Создаем структуру проекта
def create_project_structure():
    base_dir = "lolz-forum"
    
    # Удаляем старую папку если есть
    if os.path.exists(base_dir):
        print(f"⚠️  Папка {base_dir} уже существует. Удаляю...")
        shutil.rmtree(base_dir)
    
    # Структура папок
    folders = [
        f"{base_dir}/app",
        f"{base_dir}/app/forum/[category]",
        f"{base_dir}/app/thread/[id]",
        f"{base_dir}/app/api/threads",
        f"{base_dir}/app/api/posts",
        f"{base_dir}/components",
        f"{base_dir}/lib",
        f"{base_dir}/public",
    ]
    
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"✅ Создана папка: {folder}")
    
    return base_dir


# Файлы с контентом
FILES = {
    # package.json
    "package.json": '''{
  "name": "lolz-forum",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "react": "^18",
    "react-dom": "^18",
    "next": "14.0.4",
    "date-fns": "^3.0.0",
    "clsx": "^2.0.0"
  },
  "devDependencies": {
    "typescript": "^5",
    "@types/node": "^20",
    "@types/react": "^18",
    "@types/react-dom": "^18",
    "autoprefixer": "^10.0.1",
    "postcss": "^8",
    "tailwindcss": "^3.3.0"
  }
}''',

    # tsconfig.json
    "tsconfig.json": '''{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [{ "name": "next" }],
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}''',

    # tailwind.config.ts
    "tailwind.config.ts": '''import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
export default config;''',

    # postcss.config.js
    "postcss.config.js": '''module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}''',

    # next.config.js
    "next.config.js": '''/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'api.dicebear.com',
      },
      {
        protocol: 'https',
        hostname: 'via.placeholder.com',
      },
    ],
  },
}
module.exports = nextConfig''',

    # .gitignore
    ".gitignore": '''node_modules
.next
out
.env*.local
.DS_Store''',

    # lib/types.ts
    "lib/types.ts": '''export interface User {
  id: string;
  username: string;
  avatar: string;
  isOnline: boolean;
  role: 'admin' | 'moderator' | 'user';
  joinDate: Date;
  postCount: number;
  reputation: number;
}

export interface Thread {
  id: string;
  title: string;
  categoryId: string;
  author: User;
  createdAt: Date;
  replyCount: number;
  viewCount: number;
  likeCount: number;
  isLocked: boolean;
  isDeleted: boolean;
  isPinned: boolean;
  isHot: boolean;
  prefix?: {
    label: string;
    color: string;
  };
  lastPost?: {
    author: User;
    createdAt: Date;
  };
}

export interface Category {
  id: string;
  name: string;
  slug: string;
  description: string;
  icon: string;
  threadCount: number;
  postCount: number;
}

export interface ForumStats {
  totalThreads: number;
  totalPosts: number;
  totalUsers: number;
  onlineUsers: number;
}''',

    # lib/data.ts
    "lib/data.ts": '''import { User, Thread, Category, ForumStats } from './types';

export const mockUsers: User[] = [
  {
    id: '1',
    username: 'darkmaster',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=darkmaster',
    isOnline: true,
    role: 'user',
    joinDate: new Date('2023-01-15'),
    postCount: 1247,
    reputation: 89,
  },
  {
    id: '2',
    username: 'hacker228',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=hacker228',
    isOnline: false,
    role: 'user',
    joinDate: new Date('2023-03-20'),
    postCount: 543,
    reputation: 45,
  },
  {
    id: '3',
    username: 'admin',
    avatar: 'https://api.dicebear.com/7.x/avataaars/svg?seed=admin',
    isOnline: true,
    role: 'admin',
    joinDate: new Date('2022-01-01'),
    postCount: 3892,
    reputation: 234,
  },
];

export const mockCategories: Category[] = [
  {
    id: 'general',
    name: 'Общение',
    slug: 'general',
    description: 'Общие темы',
    icon: '💬',
    threadCount: 1247,
    postCount: 15432,
  },
  {
    id: 'marketplace',
    name: 'Маркет',
    slug: 'marketplace',
    description: 'Купля-продажа',
    icon: '🛒',
    threadCount: 892,
    postCount: 8921,
  },
];

export const mockThreads: Thread[] = [
  {
    id: '1',
    title: 'Как спарсить CSS с защищённого сайта?',
    categoryId: 'programming',
    author: mockUsers[0],
    createdAt: new Date(Date.now() - 15 * 60 * 1000),
    replyCount: 45,
    viewCount: 892,
    likeCount: 12,
    isLocked: false,
    isDeleted: false,
    isPinned: false,
    isHot: false,
    prefix: { label: 'Вопрос', color: '#00ba78' },
    lastPost: {
      author: mockUsers[1],
      createdAt: new Date(Date.now() - 2 * 60 * 1000),
    },
  },
  {
    id: '2',
    title: 'Продам аккаунты Steam',
    categoryId: 'marketplace',
    author: mockUsers[1],
    createdAt: new Date(Date.now() - 60 * 60 * 1000),
    replyCount: 134,
    viewCount: 2341,
    likeCount: 67,
    isLocked: false,
    isDeleted: false,
    isPinned: false,
    isHot: true,
    prefix: { label: 'Продажа', color: '#ff6b6b' },
  },
];

export const forumStats: ForumStats = {
  totalThreads: 45892,
  totalPosts: 1234567,
  totalUsers: 89432,
  onlineUsers: 3847,
};''',

    # app/globals.css
    "app/globals.css": '''@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --bg-primary: #0f1419;
  --bg-secondary: #1c1f26;
  --bg-hover: #252932;
  --border: #2f3640;
  --text-primary: #e4e6eb;
  --text-secondary: #8b949e;
  --accent: #3b82f6;
  --accent-hover: #2563eb;
  --success: #10b981;
}

body {
  color: var(--text-primary);
  background: var(--bg-primary);
  font-feature-settings: "kern";
}

* {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}''',

    # app/layout.tsx
    "app/layout.tsx": '''import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/Header";
import { AuthProvider } from "@/components/AuthContext";

export const metadata: Metadata = {
  title: "LOLZ Forum",
  description: "Форум в стиле lolz.live",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ru">
      <body>
        <AuthProvider>
          <Header />
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}''',

    # app/profile/[username]/page.tsx
    "app/profile/[username]/page.tsx": '''import Image from "next/image";
import Link from "next/link";
import { mockUsers, mockThreads } from "@/lib/data";
import { formatDistanceToNow } from "date-fns";
import { ru } from "date-fns/locale";

export default function ProfilePage({ params }: { params: { username: string } }) {
  const user = mockUsers.find(u => u.username === params.username);
  
  if (!user) {
    return (
      <div className="max-w-7xl mx-auto px-6 py-16 text-center">
        <h1 className="text-2xl font-bold mb-4">Пользователь не найден</h1>
        <Link href="/" className="text-[#3b82f6] hover:underline">
          Вернуться на главную
        </Link>
      </div>
    );
  }

  const userThreads = mockThreads.filter(t => t.author.id === user.id);

  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      {/* Профиль */}
      <div className="bg-[#1c1f26] border border-[#2f3640] rounded-xl p-8 mb-6">
        <div className="flex items-start gap-6">
          <Image 
            src={user.avatar} 
            alt={user.username} 
            width={120} 
            height={120} 
            className="rounded-2xl ring-4 ring-[#2f3640]"
          />
          
          <div className="flex-1">
            <div className="flex items-center gap-3 mb-2">
              <h1 className="text-3xl font-bold">{user.username}</h1>
              {user.isOnline && (
                <span className="flex items-center gap-1.5 px-3 py-1 bg-[#10b981]/10 text-[#10b981] rounded-full text-sm">
                  <span className="w-2 h-2 bg-[#10b981] rounded-full animate-pulse"></span>
                  Онлайн
                </span>
              )}
              {user.role === 'admin' && (
                <span className="px-3 py-1 bg-red-500/10 text-red-400 rounded-full text-sm font-medium">
                  Администратор
                </span>
              )}
              {user.role === 'moderator' && (
                <span className="px-3 py-1 bg-blue-500/10 text-blue-400 rounded-full text-sm font-medium">
                  Модератор
                </span>
              )}
            </div>
            
            <div className="grid grid-cols-3 gap-6 mt-6">
              <div>
                <div className="text-2xl font-bold text-[#3b82f6]">{user.postCount}</div>
                <div className="text-sm text-[#8b949e]">Сообщений</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-[#3b82f6]">{user.reputation}</div>
                <div className="text-sm text-[#8b949e]">Репутация</div>
              </div>
              <div>
                <div className="text-2xl font-bold text-[#3b82f6]">
                  {formatDistanceToNow(user.joinDate, { locale: ru })}
                </div>
                <div className="text-sm text-[#8b949e]">На форуме</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Темы пользователя */}
      <div>
        <h2 className="text-xl font-bold mb-4">Темы пользователя ({userThreads.length})</h2>
        
        {userThreads.length === 0 ? (
          <div className="bg-[#1c1f26] border border-[#2f3640] rounded-xl p-8 text-center text-[#8b949e]">
            Пользователь пока не создал ни одной темы
          </div>
        ) : (
          <div className="space-y-2">
            {userThreads.map(thread => (
              <Link 
                key={thread.id}
                href={`/thread/${thread.id}`}
                className="block bg-[#1c1f26] border border-[#2f3640] rounded-xl p-5 hover:border-[#3b82f6]/50 transition"
              >
                <div className="flex items-start gap-3 mb-2">
                  {thread.prefix && (
                    <span 
                      className="px-2.5 py-0.5 text-xs font-semibold rounded-md text-white"
                      style={{ backgroundColor: thread.prefix.color }}
                    >
                      {thread.prefix.label}
                    </span>
                  )}
                  <h3 className="text-base font-semibold text-white hover:text-[#3b82f6] transition">
                    {thread.title}
                  </h3>
                </div>
                
                <div className="flex items-center gap-4 text-sm text-[#8b949e]">
                  <span>
                    {formatDistanceToNow(thread.createdAt, { addSuffix: true, locale: ru })}
                  </span>
                  <span className="flex items-center gap-1">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                    </svg>
                    {thread.replyCount}
                  </span>
                  <span className="flex items-center gap-1">
                    <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                    </svg>
                    {thread.likeCount}
                  </span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </div>
    </div>
  );
}''',
    "app/page.tsx": '''import ThreadList from "@/components/ThreadList";
import Sidebar from "@/components/Sidebar";
import { mockThreads } from "@/lib/data";

export default function Home() {
  return (
    <div className="max-w-[1400px] mx-auto px-5 py-5 grid grid-cols-[250px_1fr] gap-5">
      <Sidebar />
      <main>
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-2xl font-semibold text-[#e0e0e0]">Последние темы</h1>
          <button className="px-5 py-2 bg-[#00ba78] text-white rounded-lg font-semibold hover:bg-[#228e5d] transition">
            + Создать тему
          </button>
        </div>
        <ThreadList threads={mockThreads} />
      </main>
    </div>
  );
}''',

    # components/Header.tsx
    "components/Header.tsx": '''"use client";
import Link from "next/link";
import Image from "next/image";
import { useState } from "react";
import { useAuth } from "./AuthContext";
import LoginModal from "./LoginModal";
import RegisterModal from "./RegisterModal";

export default function Header() {
  const [showLogin, setShowLogin] = useState(false);
  const [showRegister, setShowRegister] = useState(false);
  const { user, logout } = useAuth();

  return (
    <>
      <header className="bg-[#1c1f26] border-b border-[#2f3640] sticky top-0 z-50 backdrop-blur-sm bg-opacity-95">
        <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
          <div className="flex items-center gap-8">
            <Link href="/" className="text-xl font-bold text-white hover:text-[#3b82f6] transition">
              CodeHub
            </Link>
            <nav className="hidden md:flex gap-1">
              <Link href="/" className="px-4 py-2 text-sm text-[#8b949e] hover:text-white hover:bg-[#252932] rounded-lg transition">
                Главная
              </Link>
              <Link href="/marketplace" className="px-4 py-2 text-sm text-[#8b949e] hover:text-white hover:bg-[#252932] rounded-lg transition">
                Маркет
              </Link>
              <Link href="/contests" className="px-4 py-2 text-sm text-[#8b949e] hover:text-white hover:bg-[#252932] rounded-lg transition">
                Конкурсы
              </Link>
            </nav>
          </div>
          
          {user ? (
            <div className="flex items-center gap-3">
              <Link href={`/profile/${user.username}`} className="flex items-center gap-2 px-3 py-2 hover:bg-[#252932] rounded-lg transition">
                <Image src={user.avatar} alt={user.username} width={32} height={32} className="rounded-full" />
                <span className="text-sm font-medium hidden sm:block">{user.username}</span>
              </Link>
              <button 
                onClick={logout} 
                className="px-4 py-2 text-sm text-[#8b949e] hover:text-white hover:bg-[#252932] rounded-lg transition"
              >
                Выход
              </button>
            </div>
          ) : (
            <div className="flex gap-2">
              <button 
                onClick={() => setShowLogin(true)} 
                className="px-4 py-2 text-sm font-medium text-white hover:bg-[#252932] rounded-lg transition"
              >
                Войти
              </button>
              <button 
                onClick={() => setShowRegister(true)} 
                className="px-4 py-2 text-sm font-medium bg-[#3b82f6] text-white rounded-lg hover:bg-[#2563eb] transition"
              >
                Регистрация
              </button>
            </div>
          )}
        </div>
      </header>

      {showLogin && (
        <LoginModal 
          onClose={() => setShowLogin(false)} 
          onSwitchToRegister={() => { 
            setShowLogin(false); 
            setShowRegister(true); 
          }}
        />
      )}

      {showRegister && (
        <RegisterModal 
          onClose={() => setShowRegister(false)} 
          onSwitchToLogin={() => { 
            setShowRegister(false); 
            setShowLogin(true); 
          }}
        />
      )}
    </>
  );
}''',

    # app/layout.tsx
    "app/layout.tsx": '''import type { Metadata } from "next";
import "./globals.css";
import Header from "@/components/Header";
import { AuthProvider } from "@/components/AuthContext";

export const metadata: Metadata = {
  title: "CodeHub - Форум разработчиков",
  description: "Современный форум для программистов",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="ru">
      <body>
        <AuthProvider>
          <Header />
          {children}
        </AuthProvider>
      </body>
    </html>
  );
}''',

    # README.md
    "README.md": '''# CodeHub - Форум разработчиков

Современный форум на Next.js 14 + TypeScript + Tailwind

## Функционал

- Регистрация и вход (данные в localStorage)
- Профили пользователей
- Список тем и обсуждений
- Статистика форума
- Адаптивный дизайн

## Установка

```bash
npm install
npm run dev
```

Откройте http://localhost:3000

## Структура

- `app/` - страницы (главная, профиль)
- `components/` - React компоненты
- `lib/` - типы и утилиты
''',

    # lib/auth.ts
  "lib/auth.ts": '''export interface AuthUser {
  id: string;
  username: string;
  email: string;
  avatar: string;
  role: 'user' | 'admin';
}

export const AUTH_KEY = 'lolz_auth_user';

export function saveUser(user: AuthUser) {
  localStorage.setItem(AUTH_KEY, JSON.stringify(user));
}

export function getUser(): AuthUser | null {
  if (typeof window === 'undefined') return null;
  const data = localStorage.getItem(AUTH_KEY);
  return data ? JSON.parse(data) : null;
}

export function logout() {
  localStorage.removeItem(AUTH_KEY);
}

export function register(username: string, email: string, password: string): AuthUser {
  const user: AuthUser = {
    id: Date.now().toString(),
    username,
    email,
    avatar: `https://api.dicebear.com/7.x/avataaars/svg?seed=${username}`,
    role: 'user',
  };
  saveUser(user);
  return user;
}

export function login(email: string, password: string): AuthUser | null {
  // Простая проверка - в реальности нужна БД
  const stored = getUser();
  if (stored && stored.email === email) {
    return stored;
  }
  return null;
}''',

    # components/AuthContext.tsx
    "components/AuthContext.tsx": '''"use client";
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { AuthUser, getUser, logout as logoutUser } from '@/lib/auth';

interface AuthContextType {
  user: AuthUser | null;
  setUser: (user: AuthUser | null) => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<AuthUser | null>(null);

  useEffect(() => {
    setUser(getUser());
  }, []);

  const logout = () => {
    logoutUser();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, setUser, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error('useAuth must be used within AuthProvider');
  return context;
}''',

    # components/LoginModal.tsx
    "components/LoginModal.tsx": '''"use client";
import { useState } from 'react';
import { login } from '@/lib/auth';
import { useAuth } from './AuthContext';

interface Props {
  onClose: () => void;
  onSwitchToRegister: () => void;
}

export default function LoginModal({ onClose, onSwitchToRegister }: Props) {
  const [email, setEmail] = useState('test@example.com');
  const [password, setPassword] = useState('123456');
  const [error, setError] = useState('');
  const { setUser } = useAuth();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Login attempt:', email);
    const user = login(email, password);
    if (user) {
      console.log('Login success:', user);
      setUser(user);
      onClose();
    } else {
      setError('Неверный email или пароль. Создайте аккаунт сначала.');
    }
  };

  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4" onClick={onClose}>
      <div className="bg-[#1c1f26] rounded-xl p-8 max-w-md w-full shadow-2xl" onClick={e => e.stopPropagation()}>
        <h2 className="text-2xl font-bold mb-6">Вход в аккаунт</h2>
        
        {error && (
          <div className="bg-red-500/10 border border-red-500/30 text-red-400 px-4 py-3 rounded-lg mb-4 text-sm">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2 text-[#8b949e]">Email</label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-4 py-3 bg-[#0f1419] border border-[#2f3640] rounded-lg focus:outline-none focus:border-[#3b82f6] transition text-white"
              placeholder="your@email.com"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2 text-[#8b949e]">Пароль</label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full px-4 py-3 bg-[#0f1419] border border-[#2f3640] rounded-lg focus:outline-none focus:border-[#3b82f6] transition text-white"
              placeholder="••••••••"
              required
            />
          </div>

          <button 
            type="submit" 
            className="w-full py-3 bg-[#3b82f6] text-white rounded-lg font-semibold hover:bg-[#2563eb] transition mt-6"
          >
            Войти
          </button>
        </form>

        <div className="mt-6 text-center text-sm">
          <span className="text-[#8b949e]">Нет аккаунта? </span>
          <button onClick={onSwitchToRegister} className="text-[#3b82f6] hover:underline font-medium">
            Зарегистрироваться
          </button>
        </div>
      </div>
    </div>
  );
}''',

    # components/RegisterModal.tsx
    "components/RegisterModal.tsx": '''"use client";
import { useState } from 'react';
import { register } from '@/lib/auth';
import { useAuth } from './AuthContext';

interface Props {
  onClose: () => void;
  onSwitchToLogin: () => void;
}

export default function RegisterModal({ onClose, onSwitchToLogin }: Props) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const { setUser } = useAuth();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (password !== confirmPassword) {
      setError('Пароли не совпадают');
      return;
    }

    if (password.length < 6) {
      setError('Пароль минимум 6 символов');
      return;
    }

    console.log('Registering user:', { username, email });
    const user = register(username, email, password);
    console.log('User registered:', user);
    setUser(user);
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black/70 flex items-center justify-center z-50 p-4" onClick={onClose}>
      <div className="bg-[#1c1f26] rounded-xl p-8 max-w-md w-full shadow-2xl" onClick={e => e.stopPropagation()}>
        <h2 className="text-2xl font-bold mb-6">Создать аккаунт</h2>
        
        {error && (
          <div className="bg-red-500/10 border border-red-500/30 text-red-400 px-4 py-3 rounded-lg mb-4 text-sm">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2 text-[#8b949e]">Имя пользователя</label>
            <input
              type="text"
              value={username}
              onChange={e => setUsername(e.target.value)}
              className="w-full px-4 py-3 bg-[#0f1419] border border-[#2f3640] rounded-lg focus:outline-none focus:border-[#3b82f6] transition text-white"
              placeholder="username"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2 text-[#8b949e]">Email</label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-4 py-3 bg-[#0f1419] border border-[#2f3640] rounded-lg focus:outline-none focus:border-[#3b82f6] transition text-white"
              placeholder="your@email.com"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2 text-[#8b949e]">Пароль</label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full px-4 py-3 bg-[#0f1419] border border-[#2f3640] rounded-lg focus:outline-none focus:border-[#3b82f6] transition text-white"
              placeholder="••••••••"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2 text-[#8b949e]">Повторите пароль</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={e => setConfirmPassword(e.target.value)}
              className="w-full px-4 py-3 bg-[#0f1419] border border-[#2f3640] rounded-lg focus:outline-none focus:border-[#3b82f6] transition text-white"
              placeholder="••••••••"
              required
            />
          </div>

          <button 
            type="submit" 
            className="w-full py-3 bg-[#3b82f6] text-white rounded-lg font-semibold hover:bg-[#2563eb] transition mt-6"
          >
            Зарегистрироваться
          </button>
        </form>

        <div className="mt-6 text-center text-sm">
          <span className="text-[#8b949e]">Уже есть аккаунт? </span>
          <button onClick={onSwitchToLogin} className="text-[#3b82f6] hover:underline font-medium">
            Войти
          </button>
        </div>
      </div>
    </div>
  );
}''',
    "components/LoginModal.tsx": '''"use client";
import { useState } from 'react';
import { login } from '@/lib/auth';
import { useAuth } from './AuthContext';

interface Props {
  onClose: () => void;
  onSwitchToRegister: () => void;
}

export default function LoginModal({ onClose, onSwitchToRegister }: Props) {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { setUser } = useAuth();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    const user = login(email, password);
    if (user) {
      setUser(user);
      onClose();
    } else {
      setError('Неверный email или пароль');
    }
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50" onClick={onClose}>
      <div className="bg-[#272727] rounded-lg p-8 max-w-md w-full mx-4" onClick={e => e.stopPropagation()}>
        <h2 className="text-2xl font-bold mb-6">Вход</h2>
        
        {error && (
          <div className="bg-red-500/20 border border-red-500 text-red-500 px-4 py-2 rounded mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Email</label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-4 py-2 bg-[#2d2d2d] border border-[#363636] rounded-lg focus:outline-none focus:border-[#00ba78]"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Пароль</label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full px-4 py-2 bg-[#2d2d2d] border border-[#363636] rounded-lg focus:outline-none focus:border-[#00ba78]"
              required
            />
          </div>

          <button type="submit" className="w-full py-3 bg-[#00ba78] rounded-lg font-semibold hover:bg-[#228e5d] transition">
            Войти
          </button>
        </form>

        <div className="mt-4 text-center text-sm">
          <span className="text-[#949494]">Нет аккаунта? </span>
          <button onClick={onSwitchToRegister} className="text-[#00ba78] hover:underline">
            Зарегистрироваться
          </button>
        </div>
      </div>
    </div>
  );
}''',

    # components/RegisterModal.tsx
    "components/RegisterModal.tsx": '''"use client";
import { useState } from 'react';
import { register } from '@/lib/auth';
import { useAuth } from './AuthContext';

interface Props {
  onClose: () => void;
  onSwitchToLogin: () => void;
}

export default function RegisterModal({ onClose, onSwitchToLogin }: Props) {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const { setUser } = useAuth();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (password !== confirmPassword) {
      setError('Пароли не совпадают');
      return;
    }

    if (password.length < 6) {
      setError('Пароль должен быть минимум 6 символов');
      return;
    }

    const user = register(username, email, password);
    setUser(user);
    onClose();
  };

  return (
    <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50" onClick={onClose}>
      <div className="bg-[#272727] rounded-lg p-8 max-w-md w-full mx-4" onClick={e => e.stopPropagation()}>
        <h2 className="text-2xl font-bold mb-6">Регистрация</h2>
        
        {error && (
          <div className="bg-red-500/20 border border-red-500 text-red-500 px-4 py-2 rounded mb-4">
            {error}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium mb-2">Имя пользователя</label>
            <input
              type="text"
              value={username}
              onChange={e => setUsername(e.target.value)}
              className="w-full px-4 py-2 bg-[#2d2d2d] border border-[#363636] rounded-lg focus:outline-none focus:border-[#00ba78]"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Email</label>
            <input
              type="email"
              value={email}
              onChange={e => setEmail(e.target.value)}
              className="w-full px-4 py-2 bg-[#2d2d2d] border border-[#363636] rounded-lg focus:outline-none focus:border-[#00ba78]"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Пароль</label>
            <input
              type="password"
              value={password}
              onChange={e => setPassword(e.target.value)}
              className="w-full px-4 py-2 bg-[#2d2d2d] border border-[#363636] rounded-lg focus:outline-none focus:border-[#00ba78]"
              required
            />
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Повторите пароль</label>
            <input
              type="password"
              value={confirmPassword}
              onChange={e => setConfirmPassword(e.target.value)}
              className="w-full px-4 py-2 bg-[#2d2d2d] border border-[#363636] rounded-lg focus:outline-none focus:border-[#00ba78]"
              required
            />
          </div>

          <button type="submit" className="w-full py-3 bg-[#00ba78] rounded-lg font-semibold hover:bg-[#228e5d] transition">
            Зарегистрироваться
          </button>
        </form>

        <div className="mt-4 text-center text-sm">
          <span className="text-[#949494]">Уже есть аккаунт? </span>
          <button onClick={onSwitchToLogin} className="text-[#00ba78] hover:underline">
            Войти
          </button>
        </div>
      </div>
    </div>
  );
}''',
    "components/Sidebar.tsx": '''import { forumStats } from "@/lib/data";

export default function Sidebar() {
  return (
    <aside className="bg-[#272727] rounded-lg p-5 h-fit sticky top-20">
      <h3 className="text-sm font-semibold mb-3 text-[#e0e0e0]">Статистика</h3>
      <div className="bg-[#2d2d2d] p-4 rounded-lg space-y-2 text-xs">
        <div className="flex justify-between">
          <span className="text-[#949494]">Тем:</span>
          <span className="text-[#00ba78] font-semibold">{forumStats.totalThreads.toLocaleString()}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-[#949494]">Постов:</span>
          <span className="text-[#00ba78] font-semibold">{forumStats.totalPosts.toLocaleString()}</span>
        </div>
        <div className="flex justify-between">
          <span className="text-[#949494]">Онлайн:</span>
          <span className="text-[#00ba78] font-semibold">{forumStats.onlineUsers.toLocaleString()}</span>
        </div>
      </div>
    </aside>
  );
}''',

    # components/ThreadList.tsx
    "components/ThreadList.tsx": '''import Link from "next/link";
import Image from "next/image";
import { Thread } from "@/lib/types";
import { formatDistanceToNow } from "date-fns";
import { ru } from "date-fns/locale";

interface Props {
  threads: Thread[];
}

export default function ThreadList({ threads }: Props) {
  return (
    <div className="space-y-2">
      {threads.map((thread) => (
        <article 
          key={thread.id} 
          className="bg-[#1c1f26] border border-[#2f3640] rounded-xl p-5 hover:border-[#3b82f6]/50 transition group"
        >
          <div className="flex gap-4">
            <Link href={`/user/${thread.author.username}`} className="shrink-0">
              <Image 
                src={thread.author.avatar} 
                alt={thread.author.username} 
                width={48} 
                height={48} 
                className="rounded-full ring-2 ring-[#2f3640] group-hover:ring-[#3b82f6]/30 transition" 
              />
            </Link>
            
            <div className="flex-1 min-w-0">
              <div className="flex items-start gap-2 mb-2">
                {thread.prefix && (
                  <span 
                    className="px-2.5 py-0.5 text-xs font-semibold rounded-md text-white shrink-0"
                    style={{ backgroundColor: thread.prefix.color }}
                  >
                    {thread.prefix.label}
                  </span>
                )}
                <Link 
                  href={`/thread/${thread.id}`} 
                  className="text-base font-semibold text-white hover:text-[#3b82f6] transition line-clamp-2"
                >
                  {thread.title}
                </Link>
              </div>
              
              <div className="flex items-center gap-3 text-sm text-[#8b949e]">
                <Link href={`/user/${thread.author.username}`} className="hover:text-white transition font-medium">
                  {thread.author.username}
                </Link>
                {thread.author.isOnline && (
                  <span className="flex items-center gap-1">
                    <span className="w-2 h-2 bg-[#10b981] rounded-full"></span>
                    <span className="text-xs">онлайн</span>
                  </span>
                )}
                <span className="text-xs">
                  {formatDistanceToNow(thread.createdAt, { addSuffix: true, locale: ru })}
                </span>
              </div>
            </div>
            
            <div className="flex items-center gap-4 text-sm text-[#8b949e]">
              <div className="flex items-center gap-1.5">
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
                </svg>
                <span className="font-medium">{thread.replyCount}</span>
              </div>
              <div className="flex items-center gap-1.5">
                <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
                </svg>
                <span className="font-medium">{thread.likeCount}</span>
              </div>
            </div>
          </div>
        </article>
      ))}
    </div>
  );
}''',

    # components/Sidebar.tsx
    "components/Sidebar.tsx": '''import { forumStats } from "@/lib/data";

export default function Sidebar() {
  return (
    <aside className="space-y-4">
      <div className="bg-[#1c1f26] border border-[#2f3640] rounded-xl p-5">
        <h3 className="text-sm font-semibold mb-4 text-white">Статистика</h3>
        <div className="space-y-3">
          <div className="flex justify-between items-center">
            <span className="text-sm text-[#8b949e]">Тем</span>
            <span className="text-sm font-semibold text-[#3b82f6]">
              {forumStats.totalThreads.toLocaleString('ru')}
            </span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-sm text-[#8b949e]">Сообщений</span>
            <span className="text-sm font-semibold text-[#3b82f6]">
              {forumStats.totalPosts.toLocaleString('ru')}
            </span>
          </div>
          <div className="flex justify-between items-center">
            <span className="text-sm text-[#8b949e]">Пользователей</span>
            <span className="text-sm font-semibold text-[#3b82f6]">
              {forumStats.totalUsers.toLocaleString('ru')}
            </span>
          </div>
          <div className="h-px bg-[#2f3640] my-3"></div>
          <div className="flex justify-between items-center">
            <span className="text-sm text-[#8b949e]">Онлайн</span>
            <span className="text-sm font-semibold text-[#10b981] flex items-center gap-1.5">
              <span className="w-2 h-2 bg-[#10b981] rounded-full animate-pulse"></span>
              {forumStats.onlineUsers.toLocaleString('ru')}
            </span>
          </div>
        </div>
      </div>
    </aside>
  );
}''',

    # app/page.tsx
    "app/page.tsx": '''import ThreadList from "@/components/ThreadList";
import Sidebar from "@/components/Sidebar";
import { mockThreads } from "@/lib/data";

export default function Home() {
  return (
    <div className="max-w-7xl mx-auto px-6 py-8">
      <div className="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-6">
        <Sidebar />
        
        <main className="min-w-0">
          <div className="flex justify-between items-center mb-6">
            <h1 className="text-2xl font-bold">Последние темы</h1>
            <button className="px-5 py-2.5 bg-[#3b82f6] text-white text-sm font-medium rounded-lg hover:bg-[#2563eb] transition">
              Создать тему
            </button>
          </div>
          
          <ThreadList threads={mockThreads} />
        </main>
      </div>
    </div>
  );
}''',
    "components/ThreadList.tsx": '''import Link from "next/link";
import Image from "next/image";
import { Thread } from "@/lib/types";
import { formatDistanceToNow } from "date-fns";
import { ru } from "date-fns/locale";

interface Props {
  threads: Thread[];
}

export default function ThreadList({ threads }: Props) {
  return (
    <ol className="bg-[#272727] rounded-lg p-5 space-y-1">
      {threads.map((thread) => (
        <li key={thread.id} className="px-3 py-4 -mx-3 rounded-lg hover:bg-[#2d2d2d] transition relative">
          <div className="flex gap-3">
            <Image src={thread.author.avatar} alt={thread.author.username} width={52} height={52} className="rounded-lg" />
            <div className="flex-1 min-w-0">
              <div className="flex items-start gap-2 mb-1">
                {thread.prefix && (
                  <span className="px-2 py-0.5 text-xs font-semibold rounded text-white" style={{ backgroundColor: thread.prefix.color }}>
                    {thread.prefix.label}
                  </span>
                )}
                <Link href={`/thread/${thread.id}`} className="text-sm font-semibold text-[#d6d6d6] hover:text-[#e0e0e0]">
                  {thread.title}
                </Link>
                {thread.isHot && <span className="text-orange-500">🔥</span>}
                {thread.isLocked && <span className="text-yellow-600">🔒</span>}
              </div>
              <div className="text-xs text-[#949494]">
                <Link href={`/user/${thread.author.username}`} className="hover:underline">{thread.author.username}</Link>
                {thread.author.isOnline && <span className="inline-block w-2 h-2 bg-[#00ba78] rounded-full mx-1" />}
                <span>{formatDistanceToNow(thread.createdAt, { addSuffix: true, locale: ru })}</span>
              </div>
            </div>
            <div className="flex gap-3 text-xs text-[#00ba78]">
              <span>💬 {thread.replyCount}</span>
              <span>❤️ {thread.likeCount}</span>
            </div>
          </div>
        </li>
      ))}
    </ol>
  );
}''',

    # README.md
    "README.md": '''# LOLZ Forum - Next.js

Форум в стиле lolz.live на Next.js 14 + TypeScript + Tailwind

## Установка

```bash
npm install
npm run dev
```

Откройте http://localhost:3000

## Структура

- `app/` - страницы и роутинг
- `components/` - React компоненты
- `lib/` - типы и данные
'''
}


def write_files(base_dir):
    """Записываем все файлы"""
    for filepath, content in FILES.items():
        full_path = os.path.join(base_dir, filepath)
        
        # Создаем папку если нужно
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Пишем файл
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Создан файл: {filepath}")


def main():
    print("🚀 Генерация Next.js форума...\n")
    
    base_dir = create_project_structure()
    print()
    
    write_files(base_dir)
    print()
    
    print("=" * 60)
    print("✅ Проект успешно создан!")
    print("=" * 60)
    print(f"\nЧтобы запустить:")
    print(f"  cd {base_dir}")
    print(f"  npm install")
    print(f"  npm run dev")
    print(f"\nОткройте: http://localhost:3000")


if __name__ == "__main__":
    main()