export interface AuthUser {
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
}