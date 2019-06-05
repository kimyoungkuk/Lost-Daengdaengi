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
import OwnerForm1 from './components/OwnerForm1'
import OwnerForm2 from './components/OwnerForm2'
import OwnerForm3 from './components/OwnerForm3'
import OwnerForm4 from './components/OwnerForm4'
import OwnerForm5 from './components/OwnerForm5'
import OwnerForm6 from './components/OwnerForm6'
import OwnerForm7 from './components/OwnerForm7'
import OwnerForm8 from './components/OwnerForm8'
import OwnerForm9 from './components/OwnerForm9'
import OwnerForm10 from './components/OwnerForm10'
import OwnerForm11 from './components/OwnerForm11'
import f2o_recommend from './components/f2o_recommend'
import o2f_recommend from './components/o2f_recommend'
import FinishBoard from './components/FinishBoard'

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
    path: '/ownerboard/recommend/:query',
    name: 'o2f_recommend',
    component: o2f_recommend
  },
  { //
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
    path: '/ownerForm1',
    name: 'ownerForm1',
    component: OwnerForm1
  },
  {
    path: '/ownerForm2',
    name: 'ownerForm2',
    component: OwnerForm2
  },
  {
    path: '/ownerForm3',
    name: 'ownerForm3',
    component: OwnerForm3
  },
  {
    path: '/ownerForm4',
    name: 'ownerForm4',
    component: OwnerForm4
  },
  {
    path: '/ownerForm5',
    name: 'ownerForm5',
    component: OwnerForm5
  },
  {
    path: '/ownerForm6',
    name: 'ownerForm6',
    component: OwnerForm6
  },
  {
    path: '/ownerForm7',
    name: 'ownerForm7',
    component: OwnerForm7
  },
  {
    path: '/ownerForm8',
    name: 'ownerForm8',
    component: OwnerForm8
  },
  {
    path: '/ownerForm9',
    name: 'ownerForm9',
    component: OwnerForm9
  },
  {
    path: '/ownerForm10',
    name: 'ownerForm10',
    component: OwnerForm10
  },
  {
    path: '/ownerForm11',
    name: 'ownerForm11',
    component: OwnerForm11
  },
  {
    path: '*',
    redirect: '/'
  },
]