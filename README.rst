This the repository to host my code for the course `Bioinformatics
Algorithms(Part I) <https://class.coursera.org/bioinformatics-002>`_ and
the problems on `rosalind <http://rosalind.info/users/hargup/>`_. First I wrote the solutions
of 36 problems on rosalind each in separate file. I observed that there was
a lot of code duplication among files. So, I decided to compile the functions
I wrote in a package.


Why do you have SymPy as submodule?
===================================

I have been a developer at `SymPy <http://sympy.org/en/index.html>`_, a pure
python computer algebra system. I love its simple and easy too use unit testing
interface, with is based on `py.test <http://pytest.org/>`_. I wanted to maintain the same TDD(Test
Driven Development) work flow I used to follow at SymPy. With very little
modification I was able to do it.
