import HomePage from './components/HomePage'
import CounterPage from './components/CounterPage'
import AnswerSheet from './components/AnswerSheet'
import FinderBoard from './components/FinderBoard'
import OwnerBoard from './components/OwnerBoard'
import Login from './components/Login'
import AboutUs from './components/AboutUs'
import PostDetailFinder from './components/PostDetailFinder'
import PostDetailOwner from './components/PostDetailOwner'
import test from './components/test'

export default [
  { // Test Page
    path: '/test',
    name: 'test',
    component: test
  },
  { // 홈페이지
    path: '/',
    name: 'home-page',
    component: HomePage
  },
  { //
    path: '/counter',
    name: 'counter-page',
    component: CounterPage
  },
  { //
    path: '/answersheet',
    name: 'answer-sheet',
    component: AnswerSheet
  },
  { // 발견인 게시판
    path: '/finderboard',
    name: 'finderboard',
    component: FinderBoard
  },
  { // 유기견주 게시판
    path: '/ownerboard',
    name: 'ownerboard',
    component: OwnerBoard
  },
  { //
    path: '/login',
    name: 'login',
    component: Login
  },
  { //
    path: '/aboutus',
    name: 'aboutus',
    component: AboutUs
  },
  { // 유기견주 상세 페이지
    path: '/ownerboard/view/:id',
    name: 'postDetailOwner',
    component: PostDetailOwner
  },
  { // 발견인 상세 페이지
    path: '/finderboard/view/:id',
    name: 'postDetailFinder',
    component: PostDetailFinder
  },
  { //
    path: '/mp',
    name: 'parent',
    component: parent
  },
  {
    path: '*',
    redirect: '/'
  },
]