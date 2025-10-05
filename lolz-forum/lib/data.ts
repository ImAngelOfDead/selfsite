import { User, Thread, Category, ForumStats } from './types';

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
};