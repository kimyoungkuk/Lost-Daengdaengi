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
import FinishBoard from './components/FinishBoard'
import SubmitPage from './components/SubmitPage'
import test1 from './components/test1'
import test2 from './components/test2'
import adoptHome from './components/adoptHome'
import adoptPostList from './components/adoptPostList'
import adoptPostCreate from './components/adoptPostCreate'
import adoptPostDetail from './components/adoptPostDetail'
import adoptLogin from './components/adoptLogin'


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
    path: '/SubmitPage',
    name: 'SubmitPage',
    component: SubmitPage
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
    path: '/ownerboard/recommend/:query',
    name: 'o2f_recommend',
    component: o2f_recommend
  },
  { //반환완료 게시판
    path: '/finishboard',
    name: 'finishboard',
    component: FinishBoard
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
  {
    path: '*',
    redirect: '/'
  },
  {
    path: '/adopt/home',
    name: 'adoptHome',
    component: adoptHome
  },
  {//분양글게시판
    path: '/adopt/post/list',
    name: 'adoptPostList',
    component: adoptPostList
  },
  {
    path: '/adopt/post/create',
    name: 'adoptPostCreate',
    component: adoptPostCreate
  },
  {//분양글 상세페이지
    path: '/adopt/post/detail/:id',
    name: 'adoptPostDetail',
    component: adoptPostDetail
  },
  {
    path: '/adopt/login',
    name: 'adoptLogin',
    component: adoptLogin
  },
]