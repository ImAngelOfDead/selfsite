import Link from "next/link";
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
}