export interface User {
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
}