import { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory } from 'react-router-dom';
import { getFollowedPosts, getPosts } from '../../store/all_posts';
import { getChats } from '../../store/chats';
import { logout } from '../../store/session';
import SignUpForm from '../auth/SignUpForm';
import Chat from '../Chat/Chat';
import LoginModal from '../LoginModal';
import CreatePostForm from '../PostForm/CreatePostForm';
import SearchBar from '../SearchBar/SearchBar';
import './Navigation.css';

const Navigation = () => {
    const user = useSelector(state => state.session.user)
    const dispatch = useDispatch();
    const history = useHistory();
    const windowHeight = window.innerHeight;

    const chats = useSelector(state => Object.values(state.chats))
    const allPosts = useSelector(state => Object.values(state.allPosts))
    const numArr = [];
    for (let post of allPosts) numArr.push(post.id)

    const [showLoginModal, setShowLoginModal] = useState(false);
    const [showSignupModal, setShowSignupModal] = useState(false);
    const [showCreateModal, setShowCreateModal] = useState(false);
    const [showChatModal, setShowChatModal] = useState(false);

    let totalUnreadMsgs = 0;
    if (user) for (let chat of chats) for (let msg of chat.chatMessages) if (!msg.read && msg.messageOwner.id !== user.id) totalUnreadMsgs += 1;

    return (
        <div className="navigation-wrapper">
            <div className={`modal container ${showCreateModal ? "create-show" : ""}`}>
                <CreatePostForm setShowCreateModal={setShowCreateModal} showCreateModal={showCreateModal} />
            </div>
            <div
                className={`overlay ${showCreateModal ? "show" : ""}`}
                onClick={() => setShowCreateModal(!showCreateModal)}
            />
            <LoginModal showLoginModal={showLoginModal} setShowLoginModal={setShowLoginModal} />
            <div className={`modal container ${showSignupModal ? "signup-show" : ""}`}>
                <SignUpForm setShowSignupModal={setShowSignupModal} showSignupModal={showSignupModal} />
            </div>
            <div
                className={`overlay ${showSignupModal ? "show" : ""}`}
                onClick={() => setShowSignupModal(!setShowSignupModal)}
            />
            <div className={`modal container ${showChatModal ? "chat-show" : ""}`}>
                <Chat setShowChatModal={setShowChatModal} showChatModal1={showChatModal} />
            </div>
            <div
                className={`overlay ${showChatModal ? "show" : ""}`}
                onClick={() => setShowChatModal(!setShowChatModal)}
            />
            <div className="navigation-container">
                <NavLink to='/home' className='nav-logo-link'><img className='nav-logo' src='https://i.imgur.com/s9sq5Yk.png' alt='website logo' /></NavLink>
                {/* <li className='slogan'>Get your news from your friends</li> */}
                <ul className='nav-links'>
                    {!user ?
                        <li className='nav-signup-link'
                            onClick={() => history.push('/')}
                        >
                            Sign Up
                        </li>
                        :
                        <>
                            <li className='nav-login-link' onClick={() => {
                                history.push('/home')
                                dispatch(getPosts())
                            }}>All Posts</li>
                            <li className='nav-login-link' onClick={() => {
                                history.push('/my-feed')
                                dispatch(getFollowedPosts())
                            }}>My Feed</li>
                        </>
                    }
                    {user && <li className='nav-signup-link' onClick={() => {
                        setShowChatModal(true);
                        dispatch(getChats());
                    }}
                    >
                        Messages
                        {totalUnreadMsgs > 0 && <span className='unread-messages-bubble'>{totalUnreadMsgs}</span>}
                    </li>}
                    {user && <NavLink className='nav-signup-link' to={`/profile/${user.id}`}>Profile</NavLink>
                    }
                    {!user ?
                        <li className='nav-login-link-last' onClick={() => history.push('/')}>Log In</li>
                        :
                        <li className='nav-login-link-last' onClick={async () => {
                            await dispatch(logout());
                            history.push('/')
                        }}>Log Out</li>
                    }
                </ul>
                <div className='search-bar-container'>
                    <SearchBar />
                </div>
                <span
                    className='nav-create'
                    onClick={() => user ? history.push('/new-post') : setShowLoginModal(true)}
                >
                    New Post
                </span>
            </div>
        </div>
    )
}

export default Navigation;
