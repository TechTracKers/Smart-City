const express = require('express');
const authRoutes = require('./routes/auth-routes');
const profileRoutes = require('./routes/profile-routes');
const app = express();
const passportSetup = require('./config/passport-setup');
const mongoose = require('mongoose');
const cookieSession = require('cookie-session');
const crypt = require('/Users/ujjwalprakash/nodeprojects/crypt.js');
const idmongo = '0a7bbcda3fea';
const pwdmongo = '0a7bbcda3fea';
const passport = require('passport');
const bodyParser = require('body-parser');
const parser = bodyParser.urlencoded({extended : false});
const RegUser = require('./models/register-user-model');
const Promise = require('es6-promise').Promise;
const qrgen = require('../qr');
const mail = require('../email1');
const BookData = require('./models/booking-data');

mongoose.connect('mongodb://localhost:27017/parking' , function(){
  console.log('Connected to mongodb');
});

app.set('view engine' , 'ejs');

app.use(cookieSession({
  maxAge: 24*60*60*1000,
  keys: ['xyz']
}));

app.use(passport.initialize());
app.use(passport.session());

app.use('/auth' , authRoutes);
app.use('/profile' , profileRoutes);

app.get('/' , function(req,res){
  res.render('home1');
});
app.get('/home' , function(req,res){
  res.render('home1');
})
app.get('/login' , function(req , res){
  res.render('login1');
});
app.get('/register' , function(req , res){
  res.render('register');
});
app.post('/register' , parser , function(req , res , done){
  console.log(req.body);
  RegUser({
    Email: req.body.email,
    Password: req.body.password,
    Name: req.body.name,
    Mobile: req.body.mobile,
    DOB: req.body.dob
  }).save().then(function(){
    console.log('New User created');
    done();
  });
  res.render('reg-success');
});
app.post('/database/login' , parser, function(req  , res){
  console.log(req.body);
  RegUser.findOne({Email : req.body.email} , function(err , user){
    if (user == null){
      console.log('User not found');
      res.render('redirectlogin');
    }
    else{
      if(user && user.Password == req.body.password){
      console.log('Login credentials are valid');
      console.log(user);
      res.render('welcome1' , {data : user});
    } else{
      console.log('Password is incorrect');
      res.render('redirectlogin');
    }
  }
  });
});
app.post('/confirm/book' , parser , function(req , res , done){
  console.log(req.body);
  BookData({
    Name: req.body.mail,
    Email: req.body.email,
    Date: req.body.date,
    Fromtime: req.body.fromtime,
    Totime: req.body.totime,
    VehicleNo: req.body.vehicle
  }).save().then(function(){
    console.log('Booking details saved in database successfully');
    done();
  });
  qrgen('Vehicle is:' + req.body.vehicle , 'Email is:' + req.body.email);
  mail(req.body.email , 'Your booking is successful.' , 'Please refer to the attachment for the code.')
  res.render('booking-success' , {details: req.body});
});

app.listen(3000 , function(req,res){
  console.log('Server now listening at port 3000');
});
