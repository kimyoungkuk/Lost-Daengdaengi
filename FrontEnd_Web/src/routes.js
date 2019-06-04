import HomePage from './components/HomePage'
import CounterPage from './components/CounterPage'
import AnswerSheet from './components/AnswerSheet'
import FinderBoard from './components/FinderBoard'
import OwnerBoard from './components/OwnerBoard'
import Login from './components/Login'
import AboutUs from './components/AboutUs'
import PostDetailFinder from './components/PostDetailFinder'
import PostDetailOwner from './components/PostDetailOwner'
import FinderForm1 from './components/FinderForm1'
import FinderForm2 from './components/FinderForm2'
import FinderForm3 from './components/FinderForm3'
import FinderForm4 from './components/FinderForm4'
import FinderForm5 from './components/FinderForm5'
import FinderForm6 from './components/FinderForm6'
import FinderForm7 from './components/FinderForm7'
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
    path: '/finderForm1',
    name: 'finderForm1',
    component: FinderForm1
  },
  {
    path: '/finderForm2',
    name: 'finderForm2',
    component: FinderForm2
  },
  {
    path: '/finderForm3',
    name: 'finderForm3',
    component: FinderForm3
  },
  {
    path: '/finderForm4',
    name: 'finderForm4',
    component: FinderForm4
  },
  {
    path: '/finderForm5',
    name: 'finderForm5',
    component: FinderForm5
  },
  {
    path: '/finderForm6',
    name: 'finderForm6',
    component: FinderForm6
  },
  {
    path: '/finderForm7',
    name: 'finderForm7',
    component: FinderForm7
  },
  {
    path: '*',
    redirect: '/'
  },
]