import HomePage from './components/HomePage'
import CounterPage from './components/CounterPage'
import AnswerSheet from './components/AnswerSheet'
import FinderBoard from './components/FinderBoard'
import OwnerBoard from './components/OwnerBoard'
import Login from './components/Login'
import AboutUs from './components/AboutUs'
import PostDetail from './components/PostDetailFinder'

export default [
  {
    path: '/',
    name: 'home-page',
    component: HomePage
  },
  {
    path: '/counter',
    name: 'counter-page',
    component: CounterPage
  },
  {
    path: '/answersheet',
    name: 'answer-sheet',
    component: AnswerSheet
  },
  {
    path: '/finderboard',
    name: 'finderboard',
    component: FinderBoard
  },
  {
    path: '/ownerboard',
    name: 'ownerboard',
    component: OwnerBoard
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/aboutus',
    name: 'aboutus',
    component: AboutUs
  },
  {
    path: '/finderboard/view/:id',
    name: 'postDetailFinder',
    component: PostDetail
  },
  {
    path: '*',
    redirect: '/'
  }
]