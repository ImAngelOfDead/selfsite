"use client";
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
}