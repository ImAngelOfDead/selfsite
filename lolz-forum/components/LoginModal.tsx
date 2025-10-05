"use client";
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
}