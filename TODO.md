To-Do's
=======

In-Progress
-----------

- [ ] cleanup output by delegating the install to a loop based on which os_family in use
- [ ] add tests to verify that the commands themselves work (command -v cmd)

Planning
--------

- [ ] consider using `flatten` instead to speed up play execution
- [ ] fill in README
- [ ] fill in meta/main
- [ ] get molecule test command to run

Future
------

Completed
---------

- [x] make default task use `become` & edit dockerfile template to add sudo for testing
- [x] Figure out why there's permission errors in /tmp during testing
- [x] defaults
- [x] main task
- [x] test setup
- [x] test file
- [x] dockerfile template
