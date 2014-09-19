if (Meteor.isClient) {
  
  function size() {
    var h = $(window).height();
    var w = $(window).width();
    $('section').css({'top': (h - 500) / 2, 'left' : (w - 500) / 2 });
  };
  size();
  $(window).on('resize', function() {
    size()
  });

  Template.hello.rendered = function ()
{
    $(document).ready(function(){size()});
}

  Template.hello.events({
    'click .left': function () {
          var result = Meteor.call('sing');
    },
    'click .right': function () {
          var result = Meteor.call('sing');
    },
    'click .left': function () {
          var result = Meteor.call('left');
    },
    'click .hard-right': function () {
          var result = Meteor.call('hardRight');
    },
    'click .hard-left': function () {
          var result = Meteor.call('hardLeft');
    }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });

  Meteor.methods({

  sing: function () {
    fb = Npm.require('fs');
    fs.writeFile('/home/tomodo/Dropbox/robot/pipefile', 'sing');
  },
  left: function () {
      fb = Npm.require('fs');
    fs.writeFile('/home/tomodo/Dropbox/robot/pipefile', 'left');
  },
  right: function () {
      fb = Npm.require('fs');
    fs.writeFile('/home/tomodo/Dropbox/robot/pipefile', 'right');
  },
  hardLeft: function () {
      fb = Npm.require('fs');
    fs.writeFile('/home/tomodo/Dropbox/robot/pipefile', 'hard_left');
  },
  hardRight: function () {
      fb = Npm.require('fs');
    fs.writeFile('/home/tomodo/Dropbox/robot/pipefile', 'hard_right');
  }

});
}
