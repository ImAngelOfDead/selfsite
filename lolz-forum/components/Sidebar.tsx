import { forumStats } from "@/lib/data";

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
}