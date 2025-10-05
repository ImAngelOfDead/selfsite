import ThreadList from "@/components/ThreadList";
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
}