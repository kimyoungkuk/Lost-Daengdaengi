import HomePage from './components/HomePage'
import CounterPage from './components/CounterPage'
import AnswerSheet from './components/AnswerSheet'
import FinderBoard from './components/FinderBoard'
import OwnerBoard from './components/OwnerBoard'
import Login from './components/Login'
import AboutUs from './components/AboutUs'
import PostDetailFinder from './components/PostDetailFinder'
import PostDetailOwner from './components/PostDetailOwner'
import FinderForm from './components/FinderForm'
import OwnerForm from './components/OwnerForm'
import f2o_recommend from './components/f2o_recommend'
import o2f_recommend from './components/o2f_recommend'
import test1 from './components/test1'
import test2 from './components/test2'

export default [
  { // Test Page
    path: '/test1',
    name: 'test1',
    component: test1
  },
  { // Test Page
    path: '/test2',
    name: 'test2',
    component: test2
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
  { //
    path: '/finderboard/recommend/:query',
    name: 'f2o_recommend',
    component: f2o_recommend
  },
  { //
    path: '/Ownerboard/recommend/:query',
    name: 'o2f_recommend',
    component: o2f_recommend
  },
  {
    path: '/finderForm',
    name: 'finderForm',
    component: FinderForm
  },
  {
    path: '/ownerForm',
    name: 'ownerForm',
    component: OwnerForm
  },
  {
    path: '*',
    redirect: '/'
  },
]