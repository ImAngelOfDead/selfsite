import Image from "next/image";
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
}