import unittest
import subprocess
import sys
import os
import shutil
import utils


TESTDIR = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Tests(unittest.TestCase):
    def test_select_good_scoring_models(self):
        """Test select_good_scoring_models.py"""
        script = utils.get_script(TOPDIR, 'select_good_scoring_models.py')
        with utils.temporary_directory() as tmpdir:
            mod_dir = os.path.join(tmpdir, 'modeling')
            shutil.copytree(os.path.join(TESTDIR, 'modeling'), mod_dir)
            subprocess.check_call(
                [sys.executable, script,
                 '-rd', mod_dir, '-rp', 'run',
                 '-sl', 'CrossLinkingMassSpectrometryRestraint_Distance_',
                 '-pl', 'ConnectivityRestraint_Rpb1',
                 'CrossLinkingMassSpectrometryRestraint_Data_Score_Chen',
                 'ExcludedVolumeSphere_None', 'Total_Score',
                 '-alt', '1.0', '-aut', '1.0', '-mlt', '0.0', '-mut', '30.0'])
            for score in ('A', 'B'):
                score_file = os.path.join(mod_dir, 'filter',
                                          'scores%s.txt' % score)
                with open(score_file) as fh:
                    wc = len(fh.readlines())
                self.assertEqual(wc, 48)
                os.unlink(score_file)
            model_ids = os.path.join(mod_dir, 'filter', 'model_ids_scores.txt')
            with open(model_ids) as fh:
                wc = len(fh.readlines())
            self.assertEqual(wc, 97)
            os.unlink(model_ids)
            os.rmdir(os.path.join(mod_dir, 'filter'))

    def test_select_good_scoring_models_one_run(self):
        """Test select_good_scoring_models.py with only one run"""
        script = utils.get_script(TOPDIR, 'select_good_scoring_models.py')
        with utils.temporary_directory() as tmpdir:
            mod_dir = os.path.join(tmpdir, 'modeling')
            shutil.copytree(os.path.join(TESTDIR, 'modeling'), mod_dir)
            # Keep only run1
            shutil.rmtree(os.path.join(mod_dir, 'run2'))
            subprocess.check_call(
                [sys.executable, script,
                 '-rd', mod_dir, '-rp', 'run',
                 '-sl', 'CrossLinkingMassSpectrometryRestraint_Distance_',
                 '-pl', 'ConnectivityRestraint_Rpb1',
                 'CrossLinkingMassSpectrometryRestraint_Data_Score_Chen',
                 'ExcludedVolumeSphere_None', 'Total_Score',
                 '-alt', '1.0', '-aut', '1.0', '-mlt', '0.0', '-mut', '30.0'])
            # With only a single run, everything goes into sample A
            for score, exp_wc in (('A', 48), ('B', 0)):
                score_file = os.path.join(mod_dir, 'filter',
                                          'scores%s.txt' % score)
                with open(score_file) as fh:
                    wc = len(fh.readlines())
                self.assertEqual(wc, exp_wc)
                os.unlink(score_file)
            model_ids = os.path.join(mod_dir, 'filter', 'model_ids_scores.txt')
            with open(model_ids) as fh:
                wc = len(fh.readlines())
            self.assertEqual(wc, 49)
            os.unlink(model_ids)
            os.rmdir(os.path.join(mod_dir, 'filter'))

    def test_select_good_scoring_models_extract(self):
        """Test select_good_scoring_models.py with extract"""
        script = utils.get_script(TOPDIR, 'select_good_scoring_models.py')
        with utils.temporary_directory() as tmpdir:
            mod_dir = os.path.join(tmpdir, 'modeling')
            shutil.copytree(os.path.join(TESTDIR, 'modeling'), mod_dir)
            subprocess.check_call(
                [sys.executable, script,
                 '-rd', mod_dir, '-rp', 'run',
                 '-sl', 'CrossLinkingMassSpectrometryRestraint_Distance_',
                 '-pl', 'ConnectivityRestraint_Rpb1',
                 'CrossLinkingMassSpectrometryRestraint_Data_Score_Chen',
                 'ExcludedVolumeSphere_None', 'Total_Score',
                 '-alt', '1.0', '-aut', '1.0', '-mlt', '0.0', '-mut', '12.0',
                 '-e'])
            gsm_dir = os.path.join(mod_dir, 'good_scoring_models')
            for score, num in (('A', 5), ('B', 4)):
                score_file = os.path.join(gsm_dir, 'scores%s.txt' % score)
                with open(score_file) as fh:
                    wc = len(fh.readlines())
                self.assertEqual(wc, num)
                os.unlink(score_file)
            model_ids = os.path.join(gsm_dir, 'model_ids_scores.txt')
            with open(model_ids) as fh:
                wc = len(fh.readlines())
            self.assertEqual(wc, 10)
            os.unlink(model_ids)

            model_ids = os.path.join(gsm_dir, 'model_sample_ids.txt')
            with open(model_ids) as fh:
                lines = fh.readlines()
            self.assertEqual(len(lines), 9)
            for line in lines:
                num, sample = line.rstrip('\r\n').split()
                os.unlink(os.path.join(gsm_dir, 'sample_%s' % sample,
                                       '%s.rmf3' % num))
            os.unlink(model_ids)
            os.rmdir(os.path.join(gsm_dir, 'sample_A'))
            os.rmdir(os.path.join(gsm_dir, 'sample_B'))

            os.rmdir(gsm_dir)

    def test_select_good_scoring_models_extract_one_run(self):
        """Test select_good_scoring_models.py with extract, one run"""
        script = utils.get_script(TOPDIR, 'select_good_scoring_models.py')
        with utils.temporary_directory() as tmpdir:
            mod_dir = os.path.join(tmpdir, 'modeling')
            shutil.copytree(os.path.join(TESTDIR, 'modeling'), mod_dir)
            # Keep only run1
            shutil.rmtree(os.path.join(mod_dir, 'run2'))
            subprocess.check_call(
                [sys.executable, script,
                 '-rd', mod_dir, '-rp', 'run',
                 '-sl', 'CrossLinkingMassSpectrometryRestraint_Distance_',
                 '-pl', 'ConnectivityRestraint_Rpb1',
                 'CrossLinkingMassSpectrometryRestraint_Data_Score_Chen',
                 'ExcludedVolumeSphere_None', 'Total_Score',
                 '-alt', '1.0', '-aut', '1.0', '-mlt', '0.0', '-mut', '12.0',
                 '-e'])
            gsm_dir = os.path.join(mod_dir, 'good_scoring_models')
            for score, num in (('A', 2), ('B', 3)):
                score_file = os.path.join(gsm_dir, 'scores%s.txt' % score)
                with open(score_file) as fh:
                    wc = len(fh.readlines())
                self.assertEqual(wc, num)
                os.unlink(score_file)
            model_ids = os.path.join(gsm_dir, 'model_ids_scores.txt')
            with open(model_ids) as fh:
                wc = len(fh.readlines())
            self.assertEqual(wc, 6)
            os.unlink(model_ids)

            model_ids = os.path.join(gsm_dir, 'model_sample_ids.txt')
            with open(model_ids) as fh:
                lines = fh.readlines()
            self.assertEqual(len(lines), 5)
            for line in lines:
                num, sample = line.rstrip('\r\n').split()
                os.unlink(os.path.join(gsm_dir, 'sample_%s' % sample,
                                       '%s.rmf3' % num))
            os.unlink(model_ids)
            os.rmdir(os.path.join(gsm_dir, 'sample_A'))
            os.rmdir(os.path.join(gsm_dir, 'sample_B'))

            os.rmdir(gsm_dir)


if __name__ == '__main__':
    unittest.main()
